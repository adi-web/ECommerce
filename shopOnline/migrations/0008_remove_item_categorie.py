# Generated by Django 4.2.11 on 2024-06-02 16:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shopOnline", "0007_alter_item_categorie"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="categorie",
        ),
    ]
