from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
        ModelAdmin, modeladmin_register)

from .models import Item

class ItemAdmin(ModelAdmin):
    model = Item
    base_url_path = 'itemadmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Items'  # ditch this to use verbose_name_plural from model
    menu_icon = 'plus'  # change as required
    menu_order = 900  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('name', 'description', 'visible', 'price')
    list_filter = ("name", "visible")
    search_fields = ("name",)

admin.site.register(Item)
modeladmin_register(ItemAdmin)