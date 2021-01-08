from .models import Plants, Users, Nursery, UserPlant, NurseryPlant
from rest_framework import serializers
from rest_framework.serializers import Serializer


class PlantSerializer(serializers.ModelSerializer):
    #image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Plants
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'age', 'plant_name')


class NurserySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nursery
        fields = ('name', 'location', 'Plant_name')


class NurseryPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseryPlant
        fields = ('nursery_name', 'plant_name', 'price')


class UserPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlant
        fields = ('user_name', 'nursery_name', 'plant_name')