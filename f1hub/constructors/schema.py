import graphene
from graphene_django import DjangoObjectType

from .models import Constructor


class ConstructorType(DjangoObjectType):
    class Meta:
        model = Constructor


class Query(graphene.ObjectType):
    constructors = graphene.List(ConstructorType, name=graphene.String())

    def resolve_constructors(self, info, name=None, **kwargs):
        if name:
            return Constructor.objects.filter(constructorRef=name)
        return Constructor.objects.all()