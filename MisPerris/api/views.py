from django.shortcuts import render
from MisPerritos.models import Insumo
from .serializers import InsumosSerializer
from rest_framework import generics


# Create your views here.
class InsumosViewSet(generics.ListCreateAPIView):
    queryset = Insumo.objects.all()
    serializer_class = InsumosSerializer

class InsumosNameFilterViewSet(generics.ListAPIView):
    serializer_class = InsumosSerializer
    def get_queryset(self):
        name = self.kwargs['name']
        return Insumo.objects.filter(name=name)

class InsumosPriceFilterViewSet(generics.ListAPIView):
    serializer_class = InsumosSerializer
    def get_queryset(self):
        price = self.kwargs['price']
        return Insumo.objects.filter(price=price)
