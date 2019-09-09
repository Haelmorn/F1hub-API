import graphene
from graphene_django import DjangoObjectType

from .models import Driverstanding


class DriverstandingType(DjangoObjectType):
    class Meta:
        model = Driverstanding


class Query(graphene.ObjectType):
    driverstandings = graphene.List(DriverstandingType)

    def resolve_driverstandings(self, info, **kwargs):
        return Driverstanding.objects.all()