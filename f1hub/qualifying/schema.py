import graphene
from graphene_django import DjangoObjectType

from .models import Qualifying


class QualifyingType(DjangoObjectType):
    class Meta:
        model = Qualifying


class Query(graphene.ObjectType):
    qualifying = graphene.List(QualifyingType)

    def resolve_qualifying(self, info, **kwargs):
        return Qualifying.objects.all()