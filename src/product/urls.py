from django.urls import path
from .views import SearchProductList, ProductViewSet, CategoryProductViewSet, CategoryViewSet

urlpatterns = [
    path('search', SearchProductList.as_view()),
    path('', ProductViewSet.as_view({'get': 'list'})),
    path('<str:slug>', ProductViewSet.as_view({'get': 'retrieve'})),
    path('catalog/', CategoryViewSet.as_view({'get': 'list'})),
    path('catalog/<str:slug>', CategoryProductViewSet.as_view({'get': 'list'})),
]
