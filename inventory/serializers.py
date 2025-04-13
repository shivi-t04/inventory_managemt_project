from rest_framework import serializers
from .models import Item, Order, MaterialRequest, PurchaseIndent, PurchaseOrder, ReceivedStock

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MaterialRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequest
        fields = '__all__'

class PurchaseIndentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseIndent
        fields = '__all__'

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class ReceivedStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedStock
        fields = '__all__'
