from users.views import search_users, get_user_profile, get_user_chats, get_user_contacts, change_user_profile
from django.urls import path

urlpatterns = [
    path('profile/get/', get_user_profile, name='get_user_profile'),
    path('profile/change/', change_user_profile, name='change_user_profile'),
    path('chats/', get_user_chats, name='get_user_chats'),
    path('contacts/', get_user_contacts, name='get_user_contacts'),
    path('<str:nick>/', search_users, name='search_users'),
    ]
