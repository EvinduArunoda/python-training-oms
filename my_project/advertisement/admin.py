import imp
from django.contrib import admin
from .models import Advertisement

from wagtail.contrib.modeladmin.options import (
        ModelAdmin, modeladmin_register)

class AdvertisementAdmin(ModelAdmin):
    model = Advertisement
    base_url_path = 'advertisementadmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Advertisements'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 800  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('title', 'description', 'learn_more', 'bg_color')
    list_filter = ("title", "bg_color")
    search_fields = ("title",)

modeladmin_register(AdvertisementAdmin)
admin.site.register(Advertisement)
