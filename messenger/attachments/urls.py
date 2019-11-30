from attachments.views import upload_attachment, download_attachment
from django.urls import path

urlpatterns = [
    path('upload_attachment/', upload_attachment, name='upload_attachment'),
    path('download_attachment/<str:url>', download_attachment, name='download_attachment'),
    ]