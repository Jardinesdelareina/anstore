from django.urls import path
from .views import OrderView

urlpatterns = [
    path('<int:pk>', OrderView.as_view({'get': 'list', 'delete': 'destroy'})),
    path('create', OrderView.as_view({'post': 'create'}))
]
