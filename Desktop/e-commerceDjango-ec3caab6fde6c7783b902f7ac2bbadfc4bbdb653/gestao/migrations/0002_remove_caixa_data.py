# Generated by Django 4.1.7 on 2023-05-26 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caixa',
            name='data',
        ),
    ]
