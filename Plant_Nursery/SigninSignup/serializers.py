from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.db import models
from Nursery_API.models import  Users, Nursery, UserPlant, NurseryPlant
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


# Register serializer
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('__all__')
        extra_kwargs = {
            'password': {'write_only': True},
        }


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'age')


class RegisterNurserySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nursery
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }


# User serializer
class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nursery
        fields = ('name', 'location')

