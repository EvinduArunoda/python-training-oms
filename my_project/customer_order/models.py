from django.db import models
from customer.models import Customer

class CustomerOrder(models.Model):
    customer_order_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)
    order_created_date = models.DateField()
    item_count = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)