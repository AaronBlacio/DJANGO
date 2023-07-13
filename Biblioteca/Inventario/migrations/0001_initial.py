# Generated by Django 4.2.2 on 2023-07-13 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_libro', models.CharField()),
                ('nombre_autor', models.CharField()),
                ('categoria', models.CharField()),
                ('precio', models.FloatField()),
                ('codigo', models.CharField()),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
    ]
