import graphene
from graphene_django import DjangoObjectType

from .models import Circuit


class CircuitType(DjangoObjectType):
    class Meta:
        model = Circuit


class Query(graphene.ObjectType):
    circuits = graphene.List(CircuitType)

    def resolve_circuits(self, info, **kwargs):
        return Circuit.objects.all()