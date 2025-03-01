from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin

from .models import Receipt
from .serializers import ReceiptSerializer


class CashMachineViewSet(CreateModelMixin, GenericViewSet):
    queryset = Receipt.objects
    serializer_class = ReceiptSerializer
