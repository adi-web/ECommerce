# Generated by Django 4.2.11 on 2024-06-16 13:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("comment", "0007_alter_commentitem_customer_alter_commentitem_item"),
    ]

    operations = [
        migrations.RenameField(
            model_name="commentitem",
            old_name="item",
            new_name="itemComment",
        ),
    ]
