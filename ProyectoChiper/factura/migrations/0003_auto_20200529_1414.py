# Generated by Django 3.0.6 on 2020-05-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factura', '0002_productofactura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productofactura',
            old_name='catalogo',
            new_name='factura',
        ),
        migrations.AddField(
            model_name='productofactura',
            name='foto',
            field=models.CharField(default='foto', max_length=100),
        ),
    ]
