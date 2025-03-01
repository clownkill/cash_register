from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import viewsets


router_v1 = SimpleRouter()
router_v1.register("cash_machine", viewsets.CashMachineViewSet, "cash_machine")


urlpatterns = [path("", include(router_v1.urls))]
