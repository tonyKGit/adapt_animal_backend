from django.db import models

# Create your models here.
class AnimalInfo(models.Model):
    animal_id = models.IntegerField(unique=True)