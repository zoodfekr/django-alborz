from django.db import models

# Create your models here.

class World (models.Model):
    world: models.CharField(max_length=100)
    mean: models.CharField(max_length=100)
    created:models.DateTimeField()