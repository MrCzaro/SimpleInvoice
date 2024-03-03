# Generated by Django 5.0.2 on 2024-03-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="total_price_2",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="total_price_3",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
