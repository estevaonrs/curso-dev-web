# Generated by Django 4.1.7 on 2023-06-23 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0010_reforço_retirada_remove_caixaaberto_reforço_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='retirada',
            name='observacao',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Observação'),
        ),
    ]
