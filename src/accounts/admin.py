from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User, Customer, RestaurantManager, CustomerAddress, Address



class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("email",)



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("email",)




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    model = User
    list_display = ("email","is_superuser", "is_staff", "is_active","is_customer")
    list_filter = ("is_superuser", "is_staff", "is_active","is_customer")
    search_fields = ("email",)
    ordering = ("email",)
    
    
    fieldsets = (
        (None, {
            "fields": (
                "email", "password"
                )
            }
         ),
        ("Permissions", {
            "fields": (
                "is_superuser", "is_staff", "is_active", "is_customer",
                "groups", "user_permissions"
                )
            }
         ),
    )
    
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",), # collapse
            "fields": (
                # "email", "password", "is_staff", "is_superuser",
                "email", "password1", "password2", "is_staff", "is_superuser",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    
admin.site.register(User, CustomUserAdmin)






# class RestaurantManagerAdmin(admin.ModelAdmin):
#     list_display = ('email', 'date_joined', 'is_active')
#     search_fields = ('email',)

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         # return qs.filter(is_restaurant_manager=True)  # فقط نمایش مدیران رستوران

# admin.site.register(RestaurantManager, RestaurantManagerAdmin)



class RestaurantManagerAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'is_staff', 'is_active')

    def get_queryset(self, request):
        return RestaurantManager.objects.get_queryset()  # استفاده از منیجر سفارشی

admin.site.register(RestaurantManager, RestaurantManagerAdmin)



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined', 'is_staff', 'is_active')
    
    
    def get_queryset(self, request):
        return Customer.objects.all() 
    
    # def get_queryset(self, request):
    #     print("=====222")
    #     qs = super().get_queryset(request)
    #     print(len(qs))
    #     # if request.user.is_superuser:
    #     #     return qs  # اجازه دهید ادمین‌ها همه رکوردها را ببینند
    #     return qs.filter(is_customer=True)  # فقط نمایش مشتریان

admin.site.register(Customer, CustomerAdmin)





admin.site.register(CustomerAddress)
admin.site.register(Address)


