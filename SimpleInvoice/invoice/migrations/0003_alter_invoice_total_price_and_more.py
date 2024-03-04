# Generated by Django 5.0.2 on 2024-03-03 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0002_alter_invoice_total_price_2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invoice",
            name="total_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="total_price_1",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
    ]
