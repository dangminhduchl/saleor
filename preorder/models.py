from django.db import models
from saleor.order.models import Order


class Preorder(Order):
    requested_shipment_date = models.DateField(blank=True, null=True)

    class Meta:
        pass
