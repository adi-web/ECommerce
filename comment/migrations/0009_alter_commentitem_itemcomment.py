# Generated by Django 4.2.11 on 2024-06-16 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shopOnline", "0019_alter_item_description_alter_item_name"),
        ("comment", "0008_rename_item_commentitem_itemcomment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentitem",
            name="itemComment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shopOnline.item",
            ),
        ),
    ]
