from statistics import mode
from django.db import models
from item.models import Item
# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255)
    items = models.ManyToManyField(Item)
