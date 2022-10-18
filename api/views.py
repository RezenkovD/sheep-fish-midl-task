from rest_framework import viewsets
from api.serializers import PrinterSerializer, CheckSerializer
from api.models import Printer, Check


class PrintViewSet(viewsets.ModelViewSet):
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer


class CheckViewSet(viewsets.ModelViewSet):
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
