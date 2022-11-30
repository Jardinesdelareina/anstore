from django.urls import path
from .views import OrderView

urlpatterns = [
    path('all', OrderView.as_view({'get': 'list'})),
    path('<int:pk>', OrderView.as_view({'get': 'retrieve'})),
    path('create', OrderView.as_view({'post': 'create'})),
    path('delete', OrderView.as_view({'delete': 'destroy'}))
]
