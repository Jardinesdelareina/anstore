from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductView.as_view({'get': 'list'}), name='product_list'),
    path('<str:slug>', ProductView.as_view({'get': 'retrieve'}), name='product_item'),
    path('category', CategoryView.as_view({'get': 'list'}), name='category_list'),
    path('category/<str:slug>', CategoryView.as_view({'get': 'list'}), name='category_product'),
]
