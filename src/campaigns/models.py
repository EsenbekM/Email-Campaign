import pytz
from django.db import models
from django.utils import timezone

from src.common.models import BaseModel
from src.campaigns.settings import SentStatus


class Client(BaseModel):
    email = models.EmailField(null=False, blank=False, unique=True, verbose_name="Email")
    tag = models.CharField(null=False, blank=False, max_length=100, verbose_name="Tag")
    timezone = models.CharField(null=False, blank=False, max_length=100, 
                                choices=[(tz, tz) for tz in pytz.all_timezones],
                                verbose_name="Timezone")

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        db_table = "clients"
        ordering = ['created_at']


class Campaign(BaseModel):
    start_time = models.DateTimeField(null=False, blank=False, verbose_name="Start Time")
    end_time = models.DateTimeField(null=False, blank=False, verbose_name="End Time")
    message = models.TextField(null=False, blank=False, verbose_name="Message")
    time_interval_start = models.TimeField(null=False, blank=False, verbose_name="Time interval Start")
    time_interval_end = models.TimeField(null=False, blank=False, verbose_name="Time interval End")

    def is_within_time_interval(self, client_timezone: str) -> bool:
        tz = pytz.timezone(client_timezone)
        current_time = timezone.now().time()
        client_time = timezone.now().astimezone(tz).time()

        return self.time_interval_start <= current_time <= self.time_interval_end and \
               self.time_interval_start <= client_time <= self.time_interval_end

    def __str__(self):
        return f"Campaign {self.id}"
    
    class Meta:
        verbose_name = "Campaign"
        verbose_name_plural = "Campaigns"
        db_table = "campaigns"
        ordering = ['created_at']


class Message(BaseModel):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="messages", verbose_name="Campaign")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="messages", verbose_name="Client")
    sent_at = models.DateTimeField(null=True, blank=True, verbose_name="Sent At")
    status = models.CharField(max_length=10, choices=SentStatus.choices(), default='pending', verbose_name="Status")

    def __str__(self):
        return f"Message {self.id} to {self.client.email}"
    
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        db_table = "messages"
        ordering = ['created_at']
