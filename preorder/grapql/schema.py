import graphene

from saleor.graphql.core.fields import FilterInputConnectionField
from .types import Preorder


class PreorderQueries(graphene.ObjectType):
    preorders = FilterInputConnectionField(
        Preorder,
        description="haha"
    )


class PreorderMutations(graphene.ObjectType):
    from preorder.grapql.mutations import PreorderCreate
    preorder_create = PreorderCreate.Field()
