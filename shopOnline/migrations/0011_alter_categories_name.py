# Generated by Django 4.2.11 on 2024-06-02 16:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopOnline", "0010_alter_categories_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categories",
            name="name",
            field=models.CharField(
                blank=True, db_index=True, default=None, max_length=200
            ),
        ),
    ]