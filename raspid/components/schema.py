import graphene
from graphene_django import DjangoObjectType
from users.schema import UserType
from .models import Component


class ComponentType(DjangoObjectType):
    class Meta:
        model = Component


class Query(graphene.ObjectType):
    components = graphene.List(ComponentType)

    def resolve_components(self, info, **kwargs):
        return Component.objects.all()

class CreateComponent(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    cType = graphene.String()
    value = graphene.String()
    unit = graphene.String()
    owner = graphene.Field(UserType)
    
    

    #2
    class Arguments:
        name = graphene.String()
        cType = graphene.String()
        value = graphene.String()
        unit = graphene.String()
        #token = graphene.String()
        #id_user = graphene.Int()

    #3
    def mutate(self, info, name, cType, value, unit):
        #component = Component(name=name, cType=cType, value=value, unit=unit)
        #component.save()
        user = info.context.user or None

        component = Component(
            name = name,
            cType = cType,
            value = value,
            unit = unit,
            owner=user,
        )
        component.save()

        return CreateComponent( 
            id=component.id,
            name=component.name, 
            cType=component.cType, 
            value=component.value, 
            unit=component.unit,
            owner=component.owner,
        )



class UpdateData(graphene.Mutation):
    class Arguments:
        # Mutation to update a category 
        value = graphene.String(required=True)
        id = graphene.ID()


    component = graphene.Field(ComponentType)

    def mutate(self, info, value, id):
        component = Component.objects.get(pk=id)
        component.value = value
        component.save()
        
        return UpdateData(component=component)

class Mutation(graphene.ObjectType):
    create_component = CreateComponent.Field()
    update_component = UpdateData.Field()

