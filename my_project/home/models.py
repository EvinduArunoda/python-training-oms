from http.client import HTTPResponse
from pickle import TRUE
from django.db.models  import Q

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from customer.models import Customer

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        name = request.GET.get('name')

        if name == '' or name == None or name==' ':
            customers = Customer.objects.all()
        else:
            customers = Customer.objects.filter(Q(**{f'{"first_name"}__icontains':name}) | Q(**{f'{"last_name"}__icontains':name}))

        # Update template context
        context = super().get_context(request)
        context['customers'] = customers
        return context