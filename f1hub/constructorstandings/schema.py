import graphene
from graphene_django import DjangoObjectType

from .models import Constructorstanding


class ConstructorstandingType(DjangoObjectType):
    class Meta:
        model = Constructorstanding


class Query(graphene.ObjectType):
    constructorstandings = graphene.List(ConstructorstandingType)

    def resolve_constructorstandings(self, info, **kwargs):
        return Constructorstanding.objects.all()