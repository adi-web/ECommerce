from django.contrib import admin

# Register your models here.
from order.models import Order


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(Order, OrderAdmin)
