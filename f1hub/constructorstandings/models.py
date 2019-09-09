from django.db import models

# Create your models here.
class Constructorstanding(models.Model):
    constructorStandingsId = models.IntegerField(primary_key=True)
    raceId = models.ForeignKey('races.Race', on_delete=models.CASCADE)
    constructorId = models.ForeignKey('constructors.Constructor', on_delete=models.CASCADE)
    points = models.FloatField()
    position = models.IntegerField(null=True)
    positionText = models.TextField(null=True)
    wins = models.IntegerField()
