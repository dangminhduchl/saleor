import graphene
from saleor.graphql.checkout.types import Checkout
from saleor.graphql.meta.types import ObjectWithMetadata
from .. import models


class Preorder(Checkout):
    requested_shipment_date = graphene.Date(required= True,description = "date to ship")

    class Meta:
        only_fields = [
            "billing_address",
            "created",
            "discount_name",
            "gift_cards",
            "is_shipping_required",
            "last_change",
            "channel",
            "note",
            "shipping_address",
            "translated_discount_name",
            "user",
            "voucher_code",
            "discount",
            "requested_shipment_date"
        ]
        description = "Checkout object."
        model = models.Preorder
        interfaces = [graphene.relay.Node, ObjectWithMetadata]
        filter_fields = ["token"]
