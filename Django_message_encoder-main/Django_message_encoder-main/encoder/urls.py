# encoder/urls.py

from django.urls import path
from .views import encode_message

urlpatterns = [
    path('', encode_message, name='encode_message'),
]
