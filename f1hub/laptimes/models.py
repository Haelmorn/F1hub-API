from django.db import models

# Create your models here.
class Laptime(models.Model):
    raceId = models.ForeignKey('races.Race', on_delete=models.CASCADE)
    driverId = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE)
    lap = models.IntegerField(primary_key=True)
    position = models.IntegerField(null=True)
    time = models.TextField(null=True)
    milliseconds = models.TextField(null=True)