from django.db import models

# Create your models here.
class Qualifying(models.Model):
    qualifyId = models.IntegerField(primary_key=True)
    raceId = models.ForeignKey('races.Race', on_delete=models.CASCADE)
    driverId = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE)
    constructorId = models.ForeignKey('constructors.Constructor', on_delete=models.CASCADE)
    number = models.IntegerField()
    position = models.IntegerField(null=True)
    q1 = models.TextField(null=True)
    q2 = models.TextField(null=True)
    q3 = models.TextField(null=True)