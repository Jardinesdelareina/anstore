from django.urls import path
from .views import CartView

urlpatterns = [
    path('', CartView.as_view({'get': 'list'})),
    path('add', CartView.as_view({'post': 'create'})),
    path('delete/<int:product_id>/', CartView.as_view({'delete': 'destroy'})),
]
