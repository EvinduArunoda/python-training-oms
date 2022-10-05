from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["customer_id", "first_name", "last_name", "date_of_birth", "currency_balance", "page_visitis"]