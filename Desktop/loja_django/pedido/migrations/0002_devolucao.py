# Generated by Django 4.1.7 on 2023-04-20 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagamento', models.CharField(max_length=255, verbose_name='Tipo de pagamento')),
                ('observacoes', models.CharField(max_length=255, verbose_name='Observações')),
                ('itens', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.itempedido')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
            ],
            options={
                'verbose_name': 'Devolução do pedido',
                'verbose_name_plural': 'Devoluções do pedido',
            },
        ),
    ]
