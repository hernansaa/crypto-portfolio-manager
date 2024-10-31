# Generated by Django 5.1 on 2024-08-11 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolios", "0005_delete_portfolioholding"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfoliotransaction",
            name="portfolio",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transactions",
                to="portfolios.portfolio",
            ),
        ),
    ]
