from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



class MailService:
    def __init__(self, to: list, html_template: str, context: dict) -> None:
        self.to = to
        self.html_template = html_template
        self.context = context

    def message(self) -> None:
        msg = EmailMessage(
            to=self.to,
            subject='Mailing',
            body=render_to_string(self.html_template, self.context),
            from_email=settings.EMAIL_HOST_USER,
        )
        msg.content_subtype = "html"
        msg.send()