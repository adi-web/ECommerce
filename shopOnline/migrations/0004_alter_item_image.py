# Generated by Django 4.2.13 on 2024-05-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopOnline", "0003_auto_20240529_0135"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img/"),
        ),
    ]
