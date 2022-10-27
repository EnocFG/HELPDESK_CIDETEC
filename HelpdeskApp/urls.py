from django.urls import path
from . import views

app_name = 'HelpdeskApp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('<slug:ticket>/', views.ticket_single, name='ticket_single'),
]

