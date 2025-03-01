from django.contrib import admin

from . import models


class ReceiptItemInline(admin.TabularInline):
    model = models.ReceiptItem
    exclude = ("item",)
    extra = 0


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price")
    search_fields = ("title",)


@admin.register(models.Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "total_price")
    inlines = (ReceiptItemInline,)
