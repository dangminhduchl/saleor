# Generated by Django 3.2.12 on 2022-05-18 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0116_auto_20211207_0705'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='replace_product_sku',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
