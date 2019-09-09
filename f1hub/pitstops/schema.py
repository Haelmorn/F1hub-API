import graphene
from graphene_django import DjangoObjectType

from .models import Pitstop


class PitstopType(DjangoObjectType):
    class Meta:
        model = Pitstop


class Query(graphene.ObjectType):
    pitstops = graphene.List(PitstopType)

    def resolve_pitstops(self, info, **kwargs):
        return Pitstop.objects.all()