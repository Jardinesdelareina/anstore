from django.urls import path
from .views import *

urlpatterns = [
    path('product/', ProductView.as_view({'get': 'list'})),
    path('product/<str:slug>', ProductView.as_view({'get': 'retrieve'})),
    path('catalog', CategoryView.as_view({'get': 'list'})),
    path('catalog/<str:slug>', CategoryProductView.as_view({'get': 'list'})),
]
