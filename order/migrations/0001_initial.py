# Generated by Django 4.2.11 on 2024-06-03 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("shopOnline", "0017_item_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nameAddress",
                    models.CharField(blank=True, db_index=True, max_length=200),
                ),
                ("number", models.CharField(blank=True, db_index=True, max_length=200)),
                ("city", models.CharField(blank=True, db_index=True, max_length=200)),
                ("cap", models.CharField(blank=True, db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("totPay", models.FloatField()),
                ("paid", models.BooleanField(default=False)),
                (
                    "phoneNumber",
                    models.CharField(blank=True, db_index=True, max_length=200),
                ),
                (
                    "addressCustomer",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order.address",
                    ),
                ),
                ("item", models.ManyToManyField(to="shopOnline.item")),
            ],
        ),
    ]
