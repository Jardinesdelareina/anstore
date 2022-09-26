from django.urls import path
from .views import AnstoreUserViewSet

urlpatterns = [
    path('<int:pk>', AnstoreUserViewSet.as_view({
        'get': 'retrieve', 
        'put': 'update', 
        'delete': 'destroy'
    })),
]
