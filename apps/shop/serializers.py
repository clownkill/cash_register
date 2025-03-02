from collections import Counter
from datetime import datetime
from typing import Dict, Any

from django.db import transaction
from rest_framework import serializers

from shop.models import Item, Receipt, ReceiptItem
from shop.utils import generate_pdf, generate_qr_code


class ReceiptSerializer(serializers.Serializer):
    items = serializers.ListField(
        child=serializers.IntegerField(min_value=1),
        write_only=True,
    )
    qr_code_url = serializers.CharField(read_only=True)

    def validate_items(self, value):
        """Проверяем, что все переданные ID товаров существуют"""
        if not value:
            msg = "Поле 'items' не может быть пустым. Необходимо передать хотя бы один товар"
            raise serializers.ValidationError(msg)

        item_counts = Counter(value)
        items = Item.objects.in_bulk(item_counts.keys())
        missing_ids = set(item_counts.keys()) - set(items.keys())

        if missing_ids:
            raise serializers.ValidationError({"missing_items": list(missing_ids)})

        self.context["items"] = items

        return item_counts

    def create(self, validated_data: Dict[str, Any]) -> Dict[str, str]:
        item_counts = validated_data["items"]
        items = self.context["items"]
        total_price = sum(
            items[item_id].price * count for item_id, count in item_counts.items()
        )

        with transaction.atomic():
            receipt = Receipt.objects.create(total_price=total_price)
            receipt_items = [
                ReceiptItem(
                    receipt=receipt,
                    item=items[item_id],
                    title_at_time_of_purchase=items[item_id].title,
                    price_at_time_of_purchase=items[item_id].price,
                    quantity=count,
                )
                for item_id, count in item_counts.items()
            ]
            ReceiptItem.objects.bulk_create(receipt_items)

        pdf_data = {
            "items": [
                {
                    "title": ri.title_at_time_of_purchase,
                    "price": ri.price_at_time_of_purchase,
                    "quantity": ri.quantity,
                }
                for ri in receipt_items
            ],
            "total_price": total_price,
            "current_date_time": datetime.now(),
        }
        receipt.pdf_file.name = generate_pdf(pdf_data, receipt.id)
        qr_code_url = generate_qr_code(receipt)
        receipt.qr_code.name = qr_code_url.split("media/")[1]
        receipt.save()

        return {"qr_code_url": qr_code_url}
