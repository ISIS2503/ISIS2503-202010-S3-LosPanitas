# Generated by Django 2.2 on 2020-03-13 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0003_producto_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='productos',
        ),
    ]