import graphene
from graphene_django import DjangoObjectType
from django.db.models import Max

from .models import Result


class ResultType(DjangoObjectType):
    class Meta:
        model = Result


class Query(graphene.ObjectType):
    results = graphene.List(ResultType, raceId=graphene.Int(), constructor=graphene.String(), year=graphene.Int(), round=graphene.String(), driver = graphene.String(), limit=graphene.Int(), grid=graphene.Int())

    def resolve_results(self, info, raceId=None, constructor=None, year=None, round=None, driver=None, limit=999, grid=None, **kwargs):
        data = Result.objects.all()
        if raceId:
            data = data.filter(raceId=raceId)       
        if constructor:
            data = data.filter(constructorId_id__constructorRef__icontains=constructor)
        if year:
            data = data.filter(raceId_id__year=year)
        if round == "last":
            max_value = data.aggregate(Max('raceId_id__round'))['raceId_id__round__max']
            data = data.filter(raceId_id__year=year).filter(raceId_id__round=str(max_value))
        elif round != "last":
            data = data.filter(raceId_id__round=round)
        if driver:
            data = data.filter(driverId_id__driverRef__icontains=driver)
        if grid:
            data = data.filter(grid=grid)

        return data[:limit]