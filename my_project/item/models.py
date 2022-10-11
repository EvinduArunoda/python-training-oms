from email.policy import default
from statistics import mode
from django.db import models

from category.models import Category

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    visible = models.BooleanField(default=False)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
