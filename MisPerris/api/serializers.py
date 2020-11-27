from MisPerritos.models import Insumo, Contact
from rest_framework import serializers

# Modelo a serializar

class InsumosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ["id", "name", "price", "description", "stock", "created"]

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "lastname", "subject", "ctype", "message"]