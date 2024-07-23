# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Customer, RestaurantManager
from restaurant.models import Restaurant

from django.contrib.auth.mixins import PermissionRequiredMixin

from django.contrib.auth import get_user_model

User = get_user_model()



@login_required
def customer_profile(request):
    user = request.user
    if not isinstance(user, Customer):
        return redirect('home')  # یا یک صفحه مناسب دیگر
    
    context = {
        'user': user
    }
    return render(request, 'accounts/profile/customer_profile.html', context)




@login_required
def restaurant_manager_profile(request):
    user = request.user
    if not isinstance(user, RestaurantManager):
        return redirect('home')  # یا یک صفحه مناسب دیگر
    
    restaurants = Restaurant.objects.filter(manager=user)
    context = {
        'user': user,
        'restaurants': restaurants
    }
    return render(request, 'accounts/profile/manager_profile.html', context)




# ==================================
# CBV
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Customer, RestaurantManager
from restaurant.models import Restaurant



class CustomerProfileView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, DetailView):
    permission_required = 'accounts.delete_address'
    model = Customer
    template_name = 'accounts/profile/customer_profile.html'
    context_object_name = 'user'

    def test_func(self):
        # print('===========')
        # print(self.request.user.has_perm('accounts.delete_address'))
        return self.request.user.id == self.kwargs['pk'] and self.request.user.is_is_customer()
    
    def get_object(self, queryset=None):
        return Customer.objects.get(id=self.kwargs['pk'])



# class ManagerProfileView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
#     model = RestaurantManager
#     template_name = 'accounts/profile/manager_profile.html'
#     context_object_name = 'user'

#     def test_func(self):
#         return self.request.user.id == self.kwargs['pk'] and isinstance(self.request.user, RestaurantManager)
    
#     def get_object(self, queryset=None):
#         return RestaurantManager.objects.get(id=self.kwargs['pk'])

class ProfileManagerPermissionMixin(UserPassesTestMixin):
    
    def test_func(self):
        result = self.request.user.id == self.kwargs['pk'] and self.request.user.is_manager()
        return result
    
class ManagerProfileView(LoginRequiredMixin, ProfileManagerPermissionMixin, DetailView):
    model = RestaurantManager
    template_name = 'accounts/profile/manager_profile.html'
    context_object_name = 'user'
    # paginate_by = 2
    
    # profile/manag
    

    
    
    # def get_object(self, queryset=None):
    #     return RestaurantManager.objects.get(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['restaurants'] = Restaurant.objects.filter(manager=self.request.user)
        return context
    
