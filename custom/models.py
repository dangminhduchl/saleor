from django.db import models


# Create your models here.


class Custom(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    attribute = models.CharField(max_length=250)

    class Meta:
        ordering = ("name", )
