from MisPerritos.models import Insumo
from rest_framework import serializers

# Modelo a serializar

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ["id", "name", "price", "description", "stock", "created"]
