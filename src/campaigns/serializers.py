from rest_framework import serializers
from src.campaigns.models import Client, Campaign


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'email', 'tag', 'timezone')
        read_only_fields = ('id',)


class CampaignSerializer(serializers.ModelSerializer):
    total_messages = serializers.IntegerField(read_only=True)
    sent_messages = serializers.IntegerField(read_only=True)
    pending_messages = serializers.IntegerField(read_only=True)
    failed_messages = serializers.IntegerField(read_only=True)

    class Meta:
        model = Campaign
        fields = (
            'start_time', 'end_time', 'message', 
            'time_interval_start', 'time_interval_end',
            'total_messages', 'sent_messages', 
            'pending_messages', 'failed_messages'
        )