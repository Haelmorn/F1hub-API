import graphene
from graphene_django import DjangoObjectType

from .models import Race


class RaceType(DjangoObjectType):
    class Meta:
        model = Race


class Query(graphene.ObjectType):
    races = graphene.List(RaceType)

    def resolve_races(self, info, **kwargs):
        return Race.objects.all()