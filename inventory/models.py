from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    current_stock = models.PositiveIntegerField(default=0)
    reorder_level = models.PositiveIntegerField(default=10)
    
    def __str__(self):
        return self.name

class Order(models.Model):
    URGENCY_CHOICES = [
        ('routine', 'Routine'),
        ('urgent', 'Urgent'),
    ]
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='routine')
    expected_fulfillment_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    fulfilled = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Order for {self.quantity} {self.item.name}"

class MaterialRequest(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity_issued = models.PositiveIntegerField()
    issued_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Material Request for {self.order}"

class PurchaseIndent(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Purchase Indent for {self.quantity} {self.item.name}"

class PurchaseOrder(models.Model):
    indent = models.ForeignKey(PurchaseIndent, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=100)
    expected_delivery_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"PO #{self.id} for {self.indent.item.name}"

class ReceivedStock(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    quantity_received = models.PositiveIntegerField()
    vehicle_details = models.CharField(max_length=100)
    received_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Received {self.quantity_received} {self.purchase_order.indent.item.name}"
