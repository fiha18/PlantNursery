from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, UserSerializer, RegisterNurserySerializer, NurserySerializer
from django.contrib.auth.models import User


# Register API
class RegisterUserApi(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.",
        })


class RegisterNurseryApi(generics.GenericAPIView):
    serializer_class = RegisterNurserySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "Nursery": NurserySerializer(user, context=self.get_serializer_context()).data,
            "message": "Nursery Created Successfully.",
        })