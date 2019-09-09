import graphene
from graphene_django import DjangoObjectType

from .models import Driver


class DriverType(DjangoObjectType):
    class Meta:
        model = Driver


class Query(graphene.ObjectType):
    drivers = graphene.List(DriverType)

    def resolve_drivers(self, info, **kwargs):
        return Driver.objects.all()