import graphene
from graphene_django import DjangoObjectType

from .models import Circuit


class CircuitType(DjangoObjectType):
    class Meta:
        model = Circuit


class Query(graphene.ObjectType):
    circuits = graphene.List(CircuitType, name=graphene.String())

    def resolve_circuits(self, info, name=None, **kwargs):
        if name:
            return Circuit.objects.filter(name__icontains=name)
        return Circuit.objects.all()