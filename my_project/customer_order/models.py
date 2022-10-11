from re import I
from django.db import models
from customer.models import Customer

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
class CustomerOrder(models.Model):
    customer_order_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=30)
    order_created_date = models.DateField()
    item_count = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class CustomerOrderPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        customer = request.GET.get('customer')
        orders = []
        customer_data = {}
        if customer != '' or customer != None:
            customer_data = Customer.objects.get(customer_id=customer)
            orders = CustomerOrder.objects.filter(customer=customer)
            
        context = super().get_context(request)
        context['orders'] = orders
        context['customer'] = customer_data
        return context