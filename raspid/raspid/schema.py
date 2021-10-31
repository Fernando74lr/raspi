import graphene

import components.schema
import users.schema


class Query(users.schema.Query, components.schema.Query,graphene.ObjectType):
    pass


class Mutation(users.schema.Mutation, components.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)