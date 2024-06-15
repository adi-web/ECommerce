# Generated by Django 4.2.11 on 2024-06-14 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shopOnline", "0019_alter_item_description_alter_item_name"),
        ("order", "0006_remove_order_item_orderitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="item",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="shopOnline.item",
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="order.order"
            ),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
