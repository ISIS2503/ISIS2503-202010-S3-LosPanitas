# Generated by Django 2.2 on 2020-03-13 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_catalogo_productos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalogo',
            name='productos',
        ),
    ]