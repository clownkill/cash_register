from django.core.validators import FileExtensionValidator
from django.db import models


class Item(models.Model):
    """Товар"""
    title = models.CharField("Название", max_length=255, null=False, blank=False)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.title


class Receipt(models.Model):
    """Чек"""
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField("Итоговая стоимость", max_digits=10, decimal_places=2)
    pdf_file = models.FileField(upload_to="receipts/", blank=True, null=True)
    qr_code = models.FileField(upload_to="receipts/qr_codes", blank=True, null=True)

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"

    def __str__(self):
        return f"Чек #{self.pk} на {self.total_price} руб."


class ReceiptItem(models.Model):
    """Товары в чеке"""
    receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE, verbose_name="Чек", related_name="items")
    item = models.ForeignKey(
        Item,
        on_delete=models.SET_NULL,
        verbose_name="Товар",
        related_name="receipt_items",
        null=True,
        blank=True
    )
    title_at_time_of_purchase = models.CharField("Название товара", max_length=255)
    price_at_time_of_purchase = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return (f"{self.title_at_time_of_purchase} x {self.quantity} "
                f"({self.price_at_time_of_purchase} * {self.quantity} руб.)")
