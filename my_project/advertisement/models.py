from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
class Advertisement(models.Model):
    advertisement_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    learn_more = models.CharField(max_length=255)
    bg_color = models.CharField(max_length=30)

    def __str__(self) -> str:
        """Str repr of this object."""
        return self.title

class AdvertisementPage(Page):
    description = models.CharField(max_length=255)
    how_to_donate = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('how_to_donate'),
    ]
    def get_context(self, request, *args, **kwargs):
        advertisements = Advertisement.objects.all()

        context = super().get_context(request)
        context['advertisements'] = advertisements
        return  context