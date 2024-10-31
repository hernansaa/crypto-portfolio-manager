# Generated by Django 5.1 on 2024-08-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolios", "0007_alter_portfoliotransaction_transaction_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="portfolio",
            name="initial_value",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=30, null=True
            ),
        ),
    ]
