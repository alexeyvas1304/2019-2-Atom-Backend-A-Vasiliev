from user_info.views import profil, contacts
from django.urls import path

urlpatterns = [
    path('profil/', profil, name='profil'),
    path('contacts/', contacts, name='contacts'),
    ]
