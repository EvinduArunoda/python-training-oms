from rest_framework import serializers
from .models import CustomerOrder

class CustomerOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerOrder
        fields = ["customer", "description", "customer_order_id", "item_count", "order_created_date"]