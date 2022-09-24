from django.urls import path
from .views import *
from rest_framework_social_auth.google import GoogleLogin

urlpatterns = [
    path('google/', GoogleLogin.as_view(), name='google-login'),
    path('<int:pk>', AnstoreUserView.as_view({'get': 'retrieve', 'put': 'update'})),
]
