import graphene

import salgql.schema


class Query(salgql.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query) 

class Mutation(salgql.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)