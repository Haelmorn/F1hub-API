from django.db import models

# Create your models here.
class Race(models.Model):
    raceId = models.IntegerField(primary_key=True)
    year = models.IntegerField()
    round = models.IntegerField()
    circuitId = models.ForeignKey('circuits.Circuit', on_delete=models.CASCADE)
    name = models.TextField()
    date = models.TextField()
    time = models.TextField(null=True)
    url = models.TextField()