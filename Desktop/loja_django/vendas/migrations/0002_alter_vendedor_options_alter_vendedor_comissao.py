# Generated by Django 4.1.7 on 2023-04-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vendedor',
            options={'verbose_name': 'Vendedor(a)', 'verbose_name_plural': 'Vendedores'},
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='comissao',
            field=models.FloatField(),
        ),
    ]