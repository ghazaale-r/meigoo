from django.contrib import admin
from restaurant.models import Restaurant

# Register your models here.

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = ["name", "address", "open_close", "created_at", "updated_at"]
    
    empty_value_display = "-empty-"
    # fields = ["name", "address"]
    # fields = [("name", "address"), ("count_view", "order_count")]
    # exclude = ["open_close"]
    # ordering = ["-updated_at"]
    search_fields = ["name", "address"]
# admin.site.register(Restaurant, RestaurantAdmin)