import graphene
from graphene_django import DjangoObjectType

from .models import Laptime


class LaptimeType(DjangoObjectType):
    class Meta:
        model = Laptime


class Query(graphene.ObjectType):
    laptimes = graphene.List(LaptimeType)

    def resolve_laptimes(self, info, **kwargs):
        return Laptime.objects.all()