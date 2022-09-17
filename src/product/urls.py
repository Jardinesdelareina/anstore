from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view({'get': 'list'}), name='product_list'),
    path('<int:pk>/<str:slug>', ProductView.as_view({'get': 'retrieve'}), name='product_item'),
    path('category/<str:slug>', CategoryProductListView.as_view({'get': 'list'}), name='category_product'),
]
