from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list'})),
    path('<str:slug>', ProductViewSet.as_view({'get': 'retrieve'})),
    path('catalog/', CategoryViewSet.as_view({'get': 'list'})),
    path('catalog/<str:slug>', CategoryProductViewSet.as_view({'get': 'list'})),
]
