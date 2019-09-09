import graphene
from graphene_django import DjangoObjectType

from .models import Constructorresult


class ConstructorresultType(DjangoObjectType):
    class Meta:
        model = Constructorresult


class Query(graphene.ObjectType):
    constructorresults = graphene.List(ConstructorresultType)

    def resolve_constructorresults(self, info, **kwargs):
        return Constructorresult.objects.all()