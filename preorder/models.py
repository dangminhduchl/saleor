from django.db import models
from saleor.checkout.models import Checkout


class Preorder(Checkout):
    requested_shipment_date = models.DateField(blank=True, null=True)

    class Meta:
        pass
