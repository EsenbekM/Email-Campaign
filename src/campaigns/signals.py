from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from src.campaigns.models import Campaign
from src.campaigns.tasks import send_campaign_messages


@receiver(post_save, sender=Campaign)
def handle_new_campaign(sender, instance, created, **kwargs):
    if created:
        if instance.start_time <= timezone.now() <= instance.end_time:
            send_campaign_messages.delay(instance.id)
        elif instance.start_time > timezone.now():
            send_campaign_messages.apply_async((instance.id,), eta=instance.start_time)
