# Generated by Django 4.1.1 on 2022-10-03 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_account_currency_stock_description_stock_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.currency'),
        ),
    ]
