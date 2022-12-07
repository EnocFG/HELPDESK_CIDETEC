from django.urls import path
from . import views

from .views import TicketAPI

app_name = 'HelpdeskApp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:ticket>/', views.ticket_single, name='ticket_single'),
    path('ticket/api', TicketAPI.as_view(), name='ticket_api'),
]

