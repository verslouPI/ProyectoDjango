# Generated by Django 4.0.3 on 2022-08-20 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0004_alter_producto_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default='tienda/categorias/empty.jpg', upload_to='tienda'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='tienda/productos/empty.png', upload_to='tienda'),
        ),
    ]
