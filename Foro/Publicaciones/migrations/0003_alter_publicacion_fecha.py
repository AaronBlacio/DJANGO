# Generated by Django 4.2.2 on 2023-08-01 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Publicaciones', '0002_alter_publicacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(),
        ),
    ]