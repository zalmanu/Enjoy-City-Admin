from django.db import models

# Create your models here.
from djangotoolbox.fields import ListField, EmbeddedModelField
from django_mongodb_engine.storage import GridFSStorage

gridfs_storage = GridFSStorage()

class Cordinates(models.Model):
    lat = models.FloatField(null=False, blank=False)
    lng = models.FloatField(null=False, blank=False)

class City(models.Model):
    name = models.CharField(max_length=255)
    coordinates = EmbeddedModelField('Coordinates')

class Tag(models.Model):
    value = models.CharField(max_length=255)

class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(storage=gridfs_storage, upload_to='/media/categories/')

class Location(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.IntegerField()
    tags = ListField()
    coordinates = EmbeddedModelField('Coordinates')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    rating = models.PositiveSmallIntegerField(blank=True, null=True)
    photo = models.FileField(storage=gridfs_storage, upload_to='/media/locations/')

class Content(models.Model):
    location = models.IntegerField()
    description = models.TextField()
    tags = ListField()
    photo = models.FileField(storage=gridfs_storage, upload_to='/media/locations/',
                            blank=True, null=True)
