import graphene
from graphene_django import DjangoObjectType

from .models import Status


class StatusType(DjangoObjectType):
    class Meta:
        model = Status


class Query(graphene.ObjectType):
    status = graphene.List(StatusType)

    def resolve_status(self, info, **kwargs):
        return Status.objects.all()