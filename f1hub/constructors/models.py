from django.db import models

# Create your models here.
class Constructor(models.Model):
    constructorId = models.IntegerField(primary_key=True)
    constructorRef = models.TextField()
    name = models.TextField()
    nationality = models.TextField()
    url = models.TextField()