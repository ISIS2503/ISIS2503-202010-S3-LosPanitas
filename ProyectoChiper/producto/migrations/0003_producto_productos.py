# Generated by Django 2.2 on 2020-03-13 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_remove_catalogo_productos'),
        ('producto', '0002_auto_20200312_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='productos',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalogo.Catalogo'),
        ),
    ]