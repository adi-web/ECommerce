# Generated by Django 4.2.11 on 2024-06-20 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0017_orderitem_payquantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="date",
            field=models.DateField(default=datetime.date(2024, 6, 20)),
        ),
    ]
