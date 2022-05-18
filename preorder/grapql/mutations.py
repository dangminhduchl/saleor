import graphene

from preorder import models
from saleor.graphql.checkout.mutations import CheckoutCreateInput, CheckoutCreate
from saleor.graphql.core.types.common import CheckoutError


class PreorderCreateInput(CheckoutCreateInput):
    requested_shipment_date = graphene.Date(description="date to ship")


class PreorderCreate(CheckoutCreate):
    class Arguments:
        input = PreorderCreateInput(
            required=True, description="require to create preorder"
        )

    class Meta:
        description = "Create a new preorder."
        model = models.Preorder
        return_field_name = "preorder"
        error_type_class = CheckoutError
        # error_type_field = "checkout_errors"



    @classmethod
    def perform_mutation(cls, _root, info, **data):
        response  = super().perform_mutation(_root,info,**data)
        response.created = True
        return response



