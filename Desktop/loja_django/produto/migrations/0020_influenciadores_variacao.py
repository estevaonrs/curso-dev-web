# Generated by Django 4.1.7 on 2023-06-26 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0019_alter_influenciadores_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='influenciadores',
            name='variacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='produto.variacao'),
        ),
    ]