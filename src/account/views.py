from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, parsers
from .serializers import CustomUserSerializer
from .models import CustomUser


class CustomUserView(ModelViewSet):
    # Вывод профиля авторизованного пользователя
    parser_classes = (parsers.MultiPartParser,)
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
