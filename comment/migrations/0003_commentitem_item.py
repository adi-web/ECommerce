# Generated by Django 4.2.11 on 2024-06-15 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shopOnline", "0019_alter_item_description_alter_item_name"),
        ("comment", "0002_commentitem_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentitem",
            name="item",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="shopOnline.item",
            ),
        ),
    ]
