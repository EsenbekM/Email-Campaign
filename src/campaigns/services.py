from src.common.service import BaseService
from src.campaigns.models import Client, Campaign, Message


class ClientService(BaseService):
    model = Client


class CampaignService(BaseService):
    model = Campaign


class MessageService(BaseService):
    model = Message
