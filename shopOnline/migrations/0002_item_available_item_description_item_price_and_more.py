# Generated by Django 4.2.13 on 2024-05-28 22:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopOnline", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.CharField(db_index=True, default="csdc", max_length=2000),
        ),
        migrations.AddField(
            model_name="item",
            name="price",
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name="item",
            name="quantityAvailable",
            field=models.IntegerField(default=10),
        ),
    ]
