from saleor.graphql import api as core_api


def patch_schema():
    from graphene_federation import build_schema
    from .grapql.schema import (
        PreorderQueries,
        PreorderMutations
    )

    class Query(
        core_api.Query,
        PreorderQueries
    ):
        pass

    class Mutation(
        core_api.Mutation,
        PreorderMutations,
    ):
        pass

    core_api.schema = build_schema(query=Query, mutation=Mutation)


patch_schema()
schema = core_api.schema
