from django.db import models

import datetime
# Create your models here.


class Users(models.Model):
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=30)
	
	class Meta:
		managed = True
		db_table='users'


class People(models.Model):
	user = models.OneToOneField(
		Users,
		on_delete=models.CASCADE,
		primary_key=True
	)
	name = models.CharField(max_length=64) #Foto de perfil
	lastname = models.CharField(max_length=64)
	address = models.CharField(max_length=64)
	number = models.CharField(max_length=64)
	profile_pic = models.ImageField(null=True, blank=True)

	class Meta:
		managed = True
		db_table='people'

class Pets(models.Model):
	SPECIES_CHOICE = [('DO', 'Dog'), ('CA', 'Cat'), ('FE', 'Ferret'), ('RA', 'Rabbit')]
	name = models.CharField(max_length=45)
	specie = models.CharField(max_length=2, choices = SPECIES_CHOICE, default='DO')
	description = models.CharField(max_length=245)
	age = models.CharField(max_length=3)
	status = models.BooleanField(default=True)

	class Meta:
		managed = True
		db_table='pets'

class Reports(models.Model):
	placelost = models.CharField(max_length=100)
	datelost = models.DateField(("Date"), default=datetime.date.today)
	STAUTS_CHOICES = [('HO', 'HOME'), ('LO', 'LOST'), ('FO', 'FOUNDED')]
	status = models.CharField(max_length=2, choices = STAUTS_CHOICES, default='HO')
	placefounded = models.CharField(max_length=100, blank=True) #OPCIONAL
	datefounded = models.DateField(("Date"), default=datetime.date.today, blank=True)
	people_id_fkey = models.ForeignKey(People, on_delete=models.CASCADE)
	pet_id_fkey = models.ForeignKey(Pets, on_delete=models.CASCADE)

	class Meta:
		managed = True
		db_table='reports'

class Breeds(models.Model):
	pet = models.OneToOneField(
		Pets,
		on_delete=models.CASCADE,
		primary_key=True
	)

	class Meta:
		managed = True
		db_table='breeds'
