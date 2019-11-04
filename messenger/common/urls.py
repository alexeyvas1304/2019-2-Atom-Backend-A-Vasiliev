from common.views import common
from django.urls import path

urlpatterns = [
        path('', common, name='common'),
]
