from django.contrib import admin
from restaurant.models import (Restaurant, 
                               Address,
                               Category,
                               Food,
                               Menu,
                               Rating)

from django.utils.html import format_html
from django.urls import reverse

# Register your models here.

admin.site.register(Address)
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Rating)



@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ["custom_column_id_name", "custom_address", "open_close", "created_at", "updated_at", "published" ]
    # list_display_links = ("created_at", "updated_at",)
    def custom_column_id_name(self, obj):
        return f"id: {obj.id} --- name: {obj.name} "
    
    custom_column_id_name.short_description = "ID Name"
    custom_column_id_name.admin_order_field = "id"
    
    def custom_address(self, obj):
        value = obj.address
        string = value if value else "N/A"
        # return value if value else "N/A"
        return format_html('<a href={}>{}</a>', 
                           reverse('admin:restaurant_restaurant_change', args=[obj.pk]),
                           string)
    
    
    custom_address.short_description = "Address"
    custom_address.admin_order_field  = "id"
        
    empty_value_display = "-empty-" # null in db # None 
    # empty_value_display = "N/A" # null in db # None 
    # fields = ["name", "address"
    # readonly_fields = ("created_at","updated_at")
    # fields = [("name", "address"), ("count_view", "order_count"), "created_at", "updated_at", "published"]
    # exclude = ["open_close"]
    # ordering = ["-updated_at"]
    search_fields = ["name", "address"]
# admin.site.register(Restaurant, RestaurantAdmin)