# Generated by Django 4.1.7 on 2023-06-02 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0010_fiado_status_alter_fiado_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='contasreceber',
            name='status',
            field=models.CharField(choices=[('D', 'Devendo'), ('P', 'Pago')], default='D', max_length=1),
        ),
    ]
