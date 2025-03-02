from django.contrib import admin

from . import models


class ReceiptItemInline(admin.TabularInline):
    model = models.ReceiptItem
    can_delete = False
    show_change_link = False
    extra = 0
    exclude = ("item",)
    readonly_fields = (
        "title_at_time_of_purchase",
        "price_at_time_of_purchase",
        "quantity",
    )


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price")
    search_fields = ("title",)


@admin.register(models.Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "total_price")
    inlines = (ReceiptItemInline,)
