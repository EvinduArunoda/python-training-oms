from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    currency_balance = models.FloatField()
    page_visitis = models.IntegerField()

    def __str__(self) -> str:
        """Str repr of this object."""
        return self.first_name