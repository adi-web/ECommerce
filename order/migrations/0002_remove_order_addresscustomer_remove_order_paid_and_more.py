# Generated by Django 4.2.11 on 2024-06-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="addressCustomer",
        ),
        migrations.RemoveField(
            model_name="order",
            name="paid",
        ),
        migrations.RemoveField(
            model_name="order",
            name="totPay",
        ),
        migrations.AddField(
            model_name="order",
            name="addressOrder",
            field=models.CharField(blank=True, db_index=True, max_length=200),
        ),
        migrations.DeleteModel(
            name="Address",
        ),
    ]
