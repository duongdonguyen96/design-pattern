from django.db import models

class Order(models.Model):
    user_id = models.IntegerField()
    status = models.CharField(max_length=50, default="NEW")
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.FloatField()
