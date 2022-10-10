from django.contrib import admin
from .models import CustomerOrder
from wagtail.contrib.modeladmin.options import (
        ModelAdmin, modeladmin_register)
# Register your models here.

class CustomerOrderAdmin(ModelAdmin):
    model = CustomerOrder
    base_url_path = 'customerorderadmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Customer Order'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    menu_order = 700  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('description', 'order_created_date', 'item_count', 'customer')
    list_filter = ("item_count",)
    search_fields = ("customer",)
admin.site.register(CustomerOrder)
modeladmin_register(CustomerOrderAdmin)
