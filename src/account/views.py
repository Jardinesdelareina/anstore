from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import AnstoreUser
from .serializers import *


class AnstoreUserView(ModelViewSet):
    # Вывод профиля авторизованного пользователя
    serializer_class = AnstoreUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    #permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return AnstoreUser.objects.filter(id=self.request.user.id)
