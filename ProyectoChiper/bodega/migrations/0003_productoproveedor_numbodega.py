# Generated by Django 2.2 on 2020-05-29 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bodega', '0002_productoproveedor_proveedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoproveedor',
            name='numBodega',
            field=models.FloatField(default=None, null=True),
        ),
    ]