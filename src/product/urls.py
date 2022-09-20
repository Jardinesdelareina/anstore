from django.urls import path
from .views import *

urlpatterns = [
    path('product', ProductView.as_view({'get': 'list'})),
    path('product/<int:pk>', ProductView.as_view({'get': 'retrieve'})),
    path('category', CategoryView.as_view({'get': 'list'})),
    path('category/<int:category_id>', CategoryProductView.as_view({'get': 'list'})),
]
