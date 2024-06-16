from django.contrib import admin

# Register your models here.
from comment.models import CommentItem


class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(CommentItem,CommentAdmin)
