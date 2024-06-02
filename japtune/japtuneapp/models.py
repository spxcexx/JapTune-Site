from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

class CarModel(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, related_name='models', on_delete=models.CASCADE)

class CarVariant(models.Model):
    model = models.ForeignKey(CarModel, related_name='variants', on_delete=models.CASCADE)
    year = models.IntegerField()
    generation = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
