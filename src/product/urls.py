from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view({'get': 'list'})),
    path('<str:slug>', ProductView.as_view({'get': 'retrieve'})),
    path('category', CategoryView.as_view({'get': 'list'})),
    path('category/<str:slug>', ProductView.as_view({'get': 'list'})),
]
