import graphene
from graphene_django import DjangoObjectType

from .models import Constructorstanding


class ConstructorstandingType(DjangoObjectType):
    class Meta:
        model = Constructorstanding


class Query(graphene.ObjectType):
    constructorstandings = graphene.List(ConstructorstandingType, year = graphene.Int())

    def resolve_constructorstandings(self, info, year = None, **kwargs):
        data = Constructorstanding.objects.all()
        if year:
            data = data.filter(raceId_id__year=year)
        if round:
            data = data.filter(raceId_id__round=round)
        return data