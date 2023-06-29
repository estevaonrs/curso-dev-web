# Generated by Django 4.1.7 on 2023-06-02 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_alter_vendedor_comissao_alter_vendedor_vendedor'),
        ('pedido', '0010_remove_itempedido_produto_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(default='5', on_delete=django.db.models.deletion.CASCADE, to='vendas.vendedor'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('C', 'Criado'), ('A', 'Aprovado')], default='C', max_length=1),
        ),
    ]
