from django.urls import path
from .views import CustomUserView

urlpatterns = [
    path('<int:pk>', CustomUserView.as_view({
        'get': 'retrieve', 
        'put': 'update',
    })),
]
