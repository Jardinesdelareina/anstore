from django.urls import path
from .endpoints.auth_views import google_auth

urlpatterns = [
    path('', google_auth)
]