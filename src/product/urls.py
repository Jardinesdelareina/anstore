from django.urls import path
from .views import SearchProductList, ProductView, CategoryProductView, CategoryView

urlpatterns = [
    path('search', SearchProductList.as_view()),
    path('', ProductView.as_view({'get': 'list'})),
    path('<str:slug>', ProductView.as_view({'get': 'retrieve'})),
    path('catalog/', CategoryView.as_view({'get': 'list'})),
    path('catalog/<str:slug>', CategoryProductView.as_view({'get': 'list'})),
]
