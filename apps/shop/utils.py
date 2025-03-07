import os
from datetime import datetime
from typing import Dict

import pdfkit
import qrcode
from django.conf import settings
from django.template.loader import render_to_string

from shop.consts import DATETIME_FILENAME_FORMAT
from shop.exceptions import PDFGenerationError, QRGenerationError
from shop.models import Receipt


def get_timestamp_file_name(file_name: str, file_ext: str) -> str:
    timestamp = datetime.now().strftime(DATETIME_FILENAME_FORMAT)
    return f"{file_name}_{timestamp}.{file_ext}"


def generate_pdf(data: Dict, receipt_id: int) -> str:
    """Генерация PDF-чека"""
    html = render_to_string("receipt_template.html", data)
    pdf_file_name = get_timestamp_file_name(f"receipt_{receipt_id}", "pdf")
    pdf_path = os.path.join(settings.MEDIA_ROOT, f"receipts/{pdf_file_name}")
    try:
        pdfkit.from_string(html, pdf_path)
    except Exception as e:
        raise PDFGenerationError(f"Ошибка генерации PDF: {str(e)}") from e
    return f"receipts/{pdf_file_name}"


def generate_qr_code(receipt: Receipt) -> str:
    """Генерация QR-кода со ссылкой на PDF-чек"""
    pdf_url = f"{settings.SITE_URL}{settings.MEDIA_URL}{receipt.pdf_file}"
    qr_name = get_timestamp_file_name(f"qr-{receipt.id}", "png")
    qr_path = os.path.join(settings.MEDIA_ROOT, f"receipts/{qr_name}")
    try:
        qr = qrcode.make(pdf_url)
        qr.save(qr_path)
    except Exception as e:
        raise QRGenerationError(f"Ошибка генерации QR-кода: {str(e)}") from e
    return f"{settings.MEDIA_URL}receipts/{qr_name}"
