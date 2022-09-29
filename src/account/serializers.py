from rest_framework import serializers
from .models import AnstoreUser


class AnstoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnstoreUser
        exclude = ('password', 'avatar', 'groups', 'user_permissions')
