# Generated by Django 4.2.11 on 2024-06-03 22:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="CustomUser",
        ),
    ]
