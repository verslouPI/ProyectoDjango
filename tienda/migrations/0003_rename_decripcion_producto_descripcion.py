# Generated by Django 4.0.3 on 2022-08-19 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto_created_producto_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='decripcion',
            new_name='descripcion',
        ),
    ]
