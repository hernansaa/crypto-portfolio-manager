# Generated by Django 5.1 on 2024-08-11 16:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market_data", "0001_initial"),
        ("portfolios", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolioholding",
            name="asset",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="market_data.asset"
            ),
        ),
        migrations.DeleteModel(
            name="Asset",
        ),
    ]
