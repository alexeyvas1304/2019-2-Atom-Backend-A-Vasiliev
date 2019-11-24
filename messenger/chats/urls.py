from chats.views import create_chat, get_messages, add_user_to_chat, get_chat_page
from django.urls import path

urlpatterns = [
    path('create_chat/', create_chat, name='create_chat'),
    path('get_messages/<int:chat_id>/', get_messages, name='get_messages'),
    path('add_user_to_chat/', add_user_to_chat, name='add_user_to_chat'),
    path('get_chat_page/<int:chat_id>/', get_chat_page, name='get_chat_page')
    ]
