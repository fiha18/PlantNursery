from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.viewsets import ViewSet
from rest_framework import status, permissions
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import status
from .models import Plants, Users, Nursery, UserPlant, NurseryPlant
from .serializers import PlantSerializer, UserSerializer, NurserySerializer, UserPlantSerializer, NurseryPlantSerializer

# Create your views here.

'''class PlantList(APIView):

    def get(self, request):
        model = Plants.objects.all()  # Created a class UserList inherit APIView Display all the Users in HRM
        serializer = PlantSerializer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        model = Plants.objects.all()  # Created a class UserList inherit APIView Display all the Users in HRM
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''


# There is no get function only post
class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)


class PlantList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = Plants.objects.all()
    serializer_class = PlantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PlantDetail(APIView):

    def get_user(self, plant_id):
        try:
            model = Plants.objects.get(
                id=plant_id)  # Created a class UserList inherit APIView Display all the Users in HRM
            return model
        except Plants.DoesNotExist:
            return

    def get(self, request, plant_id):
        if not self.get_user(plant_id):
            return Response(f'Plant with id - {plant_id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = PlantSerializer(self.get_user(plant_id))
        return Response(serializer.data)

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)

    def put(self, request, plant_id):
        if not self.get_user(plant_id):
            return Response(f'Plant with id - {plant_id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = PlantSerializer(self.get_user(plant_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, plant_id):
        if not self.get_user(plant_id):
            return Response(f'Plant with id - {plant_id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(plant_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(APIView):

    def get_user(self, user_id):
        try:
            model = Users.objects.get(id=user_id)
            return model
        except Users.DoesNotExist:
            return

    def get(self, request, user_id):
        if not self.get_user(user_id):
            return Response(f'User with id - {user_id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(user_id))
        return Response(serializer.data)

    def put(self, request, user_id):
        if not self.get_user(user_id):
            return Response(f'User with id - {user_id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(self.get_user(user_id), data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        if not self.get_user(user_id):
            return Response(f'User with id - {user_id} is not found in database', status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(user_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NurseryList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = Nursery.objects.all()
    serializer_class = NurserySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NurseryDetail(APIView):

    def get_user(self, nursery_id):
        try:
            model = Nursery.objects.get(id=nursery_id)
            return model
        except Nursery. DoesNotExist:
            return

    def get(self, request, nursery_id):
        if not self.get_user(nursery_id):
            return Response(f'Nursery with id - {nursery_id} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = NurserySerializer(self.get_user(nursery_id))
        return Response(serializer.data)

    def put(self, request, nursery_id):
        if not self.get_user(nursery_id):
            return Response(f'Nursery with id - {nursery_id} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = NurserySerializer(self.get_user(nursery_id), data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, nursery_id):
        if not self.get_user(nursery_id):
            return Response(f'Nursery with id - {nursery_id} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        model = self.get_user(nursery_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NurseryPlantList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = NurseryPlant.objects.all()
    serializer_class = NurseryPlantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class NurseryPlantDetail(APIView):

    def get_user(self, nursery_id):
        try:
            model = NurseryPlant.objects.get(id=nursery_id)
            return model
        except NurseryPlant. DoesNotExist:
            return

    def get(self, request, nursery_id):
        if not self.get_user(nursery_id):
            return Response(f'Nursery with id - {nursery_id} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = NurseryPlantSerializer(self.get_user(nursery_id))
        return Response(serializer.data)

    def put(self, request, nursery_id):
        if not self.get_user(nursery_id):
            return Response(f'Nursery with id - {nursery_id} is not found in database',
                            status=status.HTTP_404_NOT_FOUND)
        serializer = NurseryPlantSerializer(self.get_user(nursery_id), data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserPlantList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    parser_classes = (JSONParser, MultiPartParser, FormParser)
    queryset = UserPlant.objects.all()
    serializer_class = UserPlantSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
