from django.contrib import admin
from .models import Order
from wagtail.contrib.modeladmin.options import (
        ModelAdmin, modeladmin_register)

class OrderAdmin(ModelAdmin):
    model = Order
    base_url_path = 'orderadmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Order'  # ditch this to use verbose_name_plural from model
    menu_icon = 'list-ul'  # change as required
    menu_order = 700  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('description', 'items')
    list_filter = ("order_id",)
    search_fields = ("order_id",)
    inspect_view_enabled = True

admin.site.register(Order)
modeladmin_register(OrderAdmin)