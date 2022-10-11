from django.contrib import admin
from .models import Category
from wagtail.contrib.modeladmin.options import (
        ModelAdmin, modeladmin_register)
class CategoryAdmin(ModelAdmin):
    model = Category
    base_url_path = 'categoryadmin' # customise the URL from default to admin/bookadmin
    menu_label = 'Category'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pick'  # change as required
    menu_order = 1000  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    add_to_admin_menu = True  # or False to exclude your model from the menu
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)

admin.site.register(Category)
modeladmin_register(CategoryAdmin)
