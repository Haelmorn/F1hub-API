import graphene
from graphene_django import DjangoObjectType

from .models import Season


class SeasonType(DjangoObjectType):
    class Meta:
        model = Season


class Query(graphene.ObjectType):
    seasons = graphene.List(SeasonType)

    def resolve_seasons(self, info, **kwargs):
        return Season.objects.all()