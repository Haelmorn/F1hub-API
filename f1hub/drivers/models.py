from django.db import models

# Create your models here.
class Driver(models.Model):
    driverId = models.IntegerField(primary_key=True)
    driverRef = models.TextField()
    number = models.IntegerField(null=True)
    code = models.TextField(null=True)
    forename = models.TextField()
    surname = models.TextField()
    dob = models.TextField()
    nationality = models.TextField()
    url = models.TextField()