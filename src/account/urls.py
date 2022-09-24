from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>', AnstoreUserView.as_view({'get': 'retrieve', 'put': 'update'})),
]
