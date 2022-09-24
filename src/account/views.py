from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import AnstoreUser
from .serializers import *


""" def anstore_auth(self, request):
    # Страница google-авторизации
    return render(request, 'account/google_auth.html') """


class AnstoreUserView(ModelViewSet):
    # Вывод профиля авторизованного пользователя
    serializer_class = AnstoreUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AnstoreUser.objects.filter(id=self.request.user.id)
