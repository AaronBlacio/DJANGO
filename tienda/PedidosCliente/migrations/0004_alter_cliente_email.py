# Generated by Django 4.2.2 on 2023-06-22 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PedidosCliente', '0003_alter_pedido_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='El correo'),
        ),
    ]