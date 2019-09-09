from django.db import models

# Create your models here.
class Season(models.Model):
    year = models.IntegerField(primary_key=True)
    url = models.TextField()