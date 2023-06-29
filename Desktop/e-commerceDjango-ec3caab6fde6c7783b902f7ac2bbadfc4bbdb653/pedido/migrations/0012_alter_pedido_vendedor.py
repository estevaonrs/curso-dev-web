# Generated by Django 4.1.7 on 2023-06-02 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_alter_vendedor_comissao_alter_vendedor_vendedor'),
        ('pedido', '0011_pedido_vendedor_alter_pedido_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vendas.vendedor'),
        ),
    ]