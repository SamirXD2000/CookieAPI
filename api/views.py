from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class UsersViewset(viewsets.ModelViewSet):
    queryset = models.Users.objects.all()
    serializer_class = serializers.UsersSerializer

class PeopleViewset(viewsets.ModelViewSet):
    queryset = models.People.objects.all()
    serializer_class = serializers.PeopleSerializer

class PetsViewset(viewsets.ModelViewSet):
    queryset = models.Pets.objects.all()
    serializer_class = serializers.PetsSerializer

class ReportsViewset(viewsets.ModelViewSet):
    queryset = models.Reports.objects.all()
    serializer_class = serializers.ReportsSerializer

class BreedsViewset(viewsets.ModelViewSet):
    queryset = models.Breeds.objects.all()
    serializer_class = serializers.BreedsSerializer