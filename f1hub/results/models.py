from django.db import models

# Create your models here.
class Result(models.Model):
    resultId = models.IntegerField(primary_key=True)
    raceId = models.ForeignKey('races.Race', on_delete=models.CASCADE)
    driverId = models.ForeignKey('drivers.Driver', on_delete=models.CASCADE)
    constructorId= models.ForeignKey('constructors.Constructor', on_delete=models.CASCADE)
    number = models.IntegerField()
    grid = models.IntegerField()
    position = models.TextField(null=True)
    positionText = models.TextField(null=True)
    positionOrder = models.IntegerField(null=True)
    points = models.IntegerField()
    laps = models.IntegerField()
    time = models.TextField()
    milliseconds = models.TextField()
    fastestLap = models.TextField()
    rank = models.IntegerField()
    fastestLapTime = models.TextField()
    fastestLapSpeed = models.TextField()
    statusId = models.ForeignKey('status.Status', on_delete=models.CASCADE)
