from django.urls import path
from .views import *

urlpatterns = [
    path('product', ProductView.as_view({'get': 'list'})),
    path('product/<str:product_slug>', ProductView.as_view({'get': 'retrieve'})),
    path('category', CategoryView.as_view({'get': 'list'})),
    path('category/<str:category_slug>', CategoryProductView.as_view({'get': 'list'})),
]
