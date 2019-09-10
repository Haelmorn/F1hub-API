import graphene
from graphene_django import DjangoObjectType

from .models import Circuit


class CircuitType(DjangoObjectType):
    class Meta:
        model = Circuit


class Query(graphene.ObjectType):
    circuits = graphene.List(CircuitType, name=graphene.String(), country=graphene.String())

    def resolve_circuits(self, info, name=None, country=None, **kwargs):
        data = Circuit.objects.all()
        if name:
            data = data.filter(name__icontains=name)
        if country:
            data = data.filter(country__icontains=country)
        return data