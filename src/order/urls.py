from django.urls import path
from .views import OrderViewSet

urlpatterns = [
    path('<int:pk>', OrderViewSet.as_view({
        'get': 'list',
        'post': 'create',
        'delete': 'destroy',
    }))
]
