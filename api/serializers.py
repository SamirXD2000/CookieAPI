from rest_framework import serializers;
from .models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = '__all__'

class BreedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breeds
        fields = '__all__'