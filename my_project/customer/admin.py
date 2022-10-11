from django.contrib import admin
from .models import Customer

from wagtail.contrib.modeladmin.options import (
        ModelAdmin, modeladmin_register)

class CustomerAdmin(ModelAdmin):
    model = Customer
    base_url_path = 'customeradmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Customer'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    menu_order = 600  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ('first_name', 'last_name', 'date_of_birth', 'page_visitis')
    list_filter = ("first_name",)
    search_fields = ("first_name", "last_name")

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(CustomerAdmin)
admin.site.register(Customer)