from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import AnstoreUserSerializer
from .models import AnstoreUser


class AnstorUserViewSet(ModelViewSet):
    # Вывод профиля авторизованного пользователя
    serializer_class = AnstoreUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AnstoreUser.objects.filter(id=self.request.user.id)
