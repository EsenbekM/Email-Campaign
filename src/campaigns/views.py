from django.db.models import Count, Q
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView,
)

from src.common.mixins import DeleteObjectMixin
from src.campaigns.services import ClientService, CampaignService
from src.campaigns.serializers import ClientSerializer, CampaignSerializer


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = ClientService.list(filters={"is_active": True})
    serializer_class = ClientSerializer


class ClientRetrieveUpdateDestroyAPIView(DeleteObjectMixin, RetrieveUpdateDestroyAPIView):
    queryset = ClientService.list(filters={"is_active": True})
    serializer_class = ClientSerializer

    
class CampaignListCreateAPIViewAPIView(ListCreateAPIView):
    queryset = CampaignService.list(filters={"is_active": True})
    serializer_class = CampaignSerializer

    def get_queryset(self):
        queryset = CampaignService.list(
            filters={"is_active": True},
            prefetch_=['messages']
        ).annotate(
            total_messages=Count('messages'),
            sent_messages=Count('messages', filter=Q(messages__status='sent')),
            pending_messages=Count('messages', filter=Q(messages__status='pending')),
            failed_messages=Count('messages', filter=Q(messages__status='failed'))
        )
        return queryset


class CampaignRetrieveUpdateDestroyAPIView(DeleteObjectMixin, RetrieveUpdateDestroyAPIView):
    queryset = CampaignService.list(filters={"is_active": True})
    serializer_class = CampaignSerializer

    def get_queryset(self):
        queryset = CampaignService.list(
            filters={"is_active": True},
            prefetch_=['messages']
        ).annotate(
            total_messages=Count('messages'),
            sent_messages=Count('messages', filter=Q(messages__status='sent')),
            pending_messages=Count('messages', filter=Q(messages__status='pending')),
            failed_messages=Count('messages', filter=Q(messages__status='failed'))
        )
        return queryset
    