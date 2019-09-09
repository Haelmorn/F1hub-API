from django.db import models

# Create your models here.
class Pitstop(models.Model):
    raceId = models.ForeignKey('races.Race', on_delete=models.CASCADE)
    driverId = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE)
    stop = models.IntegerField(primary_key=True)
    lap = models.IntegerField()
    time = models.TextField()
    duration= models.TextField(null=True)
    milliseconds = models.TextField(null=True)