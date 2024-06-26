import logging

from django.utils import timezone
from django.contrib.auth.models import User
from celery import shared_task

from src.campaigns.models import Campaign, Message, Client
from src.campaigns.utils import MailService
from src.campaigns.settings import SentStatus


logger = logging.getLogger("email_campaign")


@shared_task
def send_campaign_messages(campaign_id):
    logger.info(f"Starting campaign with ID {campaign_id}")

    try:
        campaign = Campaign.objects.get(id=campaign_id)
    except Campaign.DoesNotExist:
        logger.error(f"Campaign with ID {campaign_id} does not exist")
        return

    current_time = timezone.now()

    if campaign.start_time <= current_time <= campaign.end_time:
        clients = Client.objects.filter(is_active=True)
        for client in clients:
            if current_time > campaign.end_time:
                logger.info(f"Campaign {campaign_id} ended at {campaign.end_time}")
                break

            if not campaign.is_within_time_interval(client.timezone):
                continue
            
            message = Message.objects.create(
                campaign=campaign,
                client=client,
                status=SentStatus.pending
            )

            try:
                msg = MailService(
                    to=[client.email], 
                    html_template='email_template.html',
                    context={'message_text': campaign.message}
                )
                msg.message()
                message.status = SentStatus.sent
                logger.info(f"Message sent to {client.email}")

            except Exception as e:
                message.status = SentStatus.failed
                logger.exception(f"Error sending message to {client.email}: {e}")

            message.send_time = current_time
            message.save()
    else:
        logger.info(f"Campaign {campaign_id} is not in the valid time range ({campaign.start_time} - {campaign.end_time})")


@shared_task
def send_daily_campaign_statistics():
    current_date = timezone.now().date()
    campaigns = Campaign.objects.filter(created_at__date=current_date)
    stats = []

    for campaign in campaigns:
        sent_count = Message.objects.filter(campaign=campaign, status=SentStatus.sent).count()
        failed_count = Message.objects.filter(campaign=campaign, status=SentStatus.failed).count()
        pending_count = Message.objects.filter(campaign=campaign, status=SentStatus.pending).count()

        stats.append({
            'campaign_id': campaign.id,
            'campaign_date': campaign.created_at,
            'sent': sent_count,
            'failed': failed_count,
            'pending': pending_count,
        })

    admins_emails = User.objects.filter(is_superuser=True, email__isnull=False).values_list('email', flat=True)

    try:
        msg = MailService(
            to=admins_emails, 
            html_template='daily_statistics.html',
            context={'stats': stats}
        )
        msg.message()

    except Exception as e:
        logger.exception(f"Error sending daily statistics email: {e}")

