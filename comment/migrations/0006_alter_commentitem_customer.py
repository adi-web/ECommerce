# Generated by Django 4.2.11 on 2024-06-16 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comment", "0005_alter_commentitem_item"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commentitem",
            name="customer",
            field=models.ForeignKey(
                default=0,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
