# Generated by Django 5.0 on 2023-12-15 06:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('localizaciones', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Capitan',
            fields=[
                ('id_capitan', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=20)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='localizaciones.comuna')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_lider', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('ciudad', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('foto_perfil', models.CharField(max_length=255)),
                ('superusuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lideres_asignados', to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usuarios.userprofile')),
            ],
        ),
    ]
