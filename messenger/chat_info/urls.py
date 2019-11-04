from chat_info.views import chat_list, chat_page
from django.urls import path

urlpatterns = [
    path('chat_list/', chat_list, name='chat_list'),
    path('chat_page/', chat_page, name='chat_page'),
    ]