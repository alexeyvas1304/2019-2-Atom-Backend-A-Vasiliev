from users.views import search_users, get_user_profile, get_user_chats, get_user_contacts
from django.urls import path

urlpatterns = [
    path('<str:nick>/', search_users, name='search_users'),
    path('profile/<int:user_id>/', get_user_profile, name='get_user_profile'),
    path('chats/<int:user_id>/', get_user_chats, name='get_user_chats'),
    path('contacts/<int:user_id>/', get_user_contacts, name='get_user_contacts'),
    ]
