import graphene
from graphene_django import DjangoObjectType

from .models import Constructorstanding


class ConstructorstandingType(DjangoObjectType):
    class Meta:
        model = Constructorstanding


class Query(graphene.ObjectType):
    constructorstandings = graphene.List(ConstructorstandingType, round = graphene.String(), year = graphene.Int())

    def resolve_constructorstandings(self, info, year = 2019, round = "last", **kwargs):
        data = Constructorstanding.objects.all()
        if year:
            data = data.filter(raceId_id__year=year)
        if round == "last":
            max_value = data.filter(raceId_id__year=year).order_by('-raceId_id__round').first()
            data = data.filter(raceId_id__year=year).filter(raceId_id__round=str(max_value))
        elif round != "last":
            data = data.filter(raceId_id__round=round)
        return data