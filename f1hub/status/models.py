from django.db import models

# Create your models here.
class Status(models.Model):
    statusId = models.IntegerField(primary_key=True)
    status = models.TextField()
