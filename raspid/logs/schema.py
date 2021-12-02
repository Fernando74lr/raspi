import graphene
from graphene_django import DjangoObjectType
from components.schema import ComponentType
from .models import Log

class LogType(DjangoObjectType):
    class Meta:
        model = Log

class Query(graphene.ObjectType):
    logs = graphene.List(LogType)

    def resolve_logs(self, info, **kwargs):
        return Log.objects.all()

class CreateLog(graphene.Mutation):
    id = graphene.Int()
    value = graphene.String()
    component = graphene.Field(ComponentType)
    
    class Arguments:
        value = graphene.String()

    def mutate(self, info, value):
        component = component.id or None

        log = Log(
            value = value,
            component=component,
        )
        log.save()

        return CreateLog( 
            id=log.id,
            value=log.value,
            component=log.component,
        )

class Mutation(graphene.ObjectType):
    create_log = CreateLog.Field()

