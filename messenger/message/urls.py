from message.views import send_message,read_message
from django.urls import path

urlpatterns = [
    path('send_message/', send_message, name='send_message'),
    path('read_message/', read_message, name='read_message'),
    ]