from rest_framework import serializers
from .models import *


class AnstoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnstoreUser
        fields = ('username', 'email', 'phone', 'gender', 'birthday')
