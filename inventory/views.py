from rest_framework import generics
from .models import Item, Order, MaterialRequest, PurchaseIndent, PurchaseOrder, ReceivedStock
from .serializers import (
    ItemSerializer, OrderSerializer, MaterialRequestSerializer,
    PurchaseIndentSerializer, PurchaseOrderSerializer, ReceivedStockSerializer
)

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class MaterialRequestListCreateView(generics.ListCreateAPIView):
    queryset = MaterialRequest.objects.all()
    serializer_class = MaterialRequestSerializer

class PurchaseIndentListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseIndent.objects.all()
    serializer_class = PurchaseIndentSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class ReceivedStockListCreateView(generics.ListCreateAPIView):
    queryset = ReceivedStock.objects.all()
    serializer_class = ReceivedStockSerializer
