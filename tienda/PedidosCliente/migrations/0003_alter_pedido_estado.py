# Generated by Django 4.2.2 on 2023-06-22 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PedidosCliente', '0002_alter_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.BooleanField(),
        ),
    ]
