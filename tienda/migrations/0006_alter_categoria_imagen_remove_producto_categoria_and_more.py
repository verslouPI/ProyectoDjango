# Generated by Django 4.0.3 on 2022-09-02 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_categoria_descripcion_categoria_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='imagen',
            field=models.ImageField(default='tienda/categorias/empty.jpg', upload_to='tienda/categorias'),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.categoria'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='tienda/productos/empty.png', upload_to='tienda/productos'),
        ),
    ]