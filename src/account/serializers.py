from rest_framework import serializers
from .models import AnstoreUser


class AnstoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnstoreUser
        fields = (
            'id', 
            'username', 
            'email', 
            'gender', 
            'phone', 
            'is_active', 
            'created_at'
        )
