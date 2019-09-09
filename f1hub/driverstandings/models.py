from django.db import models

# Create your models here.
class Driverstanding(models.Model):
    driverStandingsId = models.IntegerField(primary_key=True)
    raceId = models.ForeignKey('races.Race', on_delete=models.CASCADE)
    driverId = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE)
    points = models.FloatField()
    position = models.IntegerField(null=True)
    positionText = models.TextField(null=True)
    wins = models.IntegerField()