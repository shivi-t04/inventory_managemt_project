from django.urls import path
from . import views

urlpatterns = [
    path('items/', views.ItemListCreateView.as_view(), name='item-list-create'),
    path('orders/', views.OrderListCreateView.as_view(), name='order-list-create'),
    path('material-requests/', views.MaterialRequestListCreateView.as_view(), name='material-request-list-create'),
    path('purchase-indents/', views.PurchaseIndentListCreateView.as_view(), name='purchase-indent-list-create'),
    path('purchase-orders/', views.PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('received-stocks/', views.ReceivedStockListCreateView.as_view(), name='received-stock-list-create'),
]
