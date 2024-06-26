from django.urls import path, include
from src.campaigns import views


urlpatterns_v1 = [
    path('clients/', views.ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', views.ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),

    path('campaign/', views.CampaignListCreateAPIViewAPIView.as_view(), name='campaign-list-create'),
    path('campaign/<int:pk>/', views.CampaignRetrieveUpdateDestroyAPIView.as_view(), name='campaign-retrieve-update-destroy')
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1)),
]