# Generated by Django 4.0.3 on 2022-08-04 09:19

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.CharField(default='81d33-179', editable=False, max_length=8, primary_key=True, serialize=False)),
                ('categoria', models.CharField(choices=[('SW', 'Software'), ('HW', 'Hardware'), ('LP', 'Lenguaje de Programación'), ('OR', 'Others')], default='SW', max_length=2)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'catergoria',
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('contenido', models.CharField(max_length=800)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=blog.models.path_file_name)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(default=2, on_delete=django.db.models.deletion.SET_DEFAULT, to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ManyToManyField(to='blog.categoria')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
