from django.contrib import admin

from src.campaigns.models import Client, Campaign, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    fields = ['id', 'email', 'tag', 'timezone', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['id', 'created_at', 'updated_at', 'is_active']
    list_display = ['id', 'email', 'tag']
    list_display_links = ['id', 'email']
    list_filter = ['is_active']
    search_fields = ['email']


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    fields = ['id', 'start_time', 'end_time', 'time_interval_start', 'time_interval_end', 'message', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['id', 'created_at', 'updated_at', 'is_active']
    list_display = ['id', 'start_time', 'end_time']
    list_display_links = ['id']
    list_filter = ['is_active']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    fields = ['id', 'campaign', 'client', 'sent_at', 'status', 'created_at', 'updated_at', 'is_active']
    readonly_fields = ['id', 'created_at', 'updated_at', 'is_active']
    list_display = ['id', 'campaign', 'client', 'status']
    list_display_links = ['id', 'campaign', 'client']
    list_filter = ['is_active', 'status']
    search_fields = ['client__email']
