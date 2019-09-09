from django.db import models

# Create your models here.
class Constructorresult(models.Model):
    constructorResultsId = models.IntegerField(primary_key=True)
    raceId = models.ForeignKey('races.Race', on_delete=models.CASCADE)
    constructorId = models.ForeignKey('constructors.Constructor', on_delete=models.CASCADE)
    points = models.FloatField()
    status = models.TextField(null=True)