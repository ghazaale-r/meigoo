# views.py
# ==================================================
#  sign up view for restauarant manager and customer

#  CUSTOMER SIGNUP

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomerSignUpForm
from .models import Customer
from django.urls import reverse

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_customer = True
            user.save()
            
            # اضافه کردن گروه‌ها
            group1, created1 = Group.objects.get_or_create(name='Customer Group 1')
            group2, created2 = Group.objects.get_or_create(name='Customer Group 2')
            user.groups.add(group1)
            user.groups.add(group2)

            login_url = reverse('accounts:login') + f'?next={reverse("accounts:customer_profile", kwargs={"pk": user.pk})}'
            return redirect(login_url)
        
            # login(request, user)
            # return redirect('home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'accounts/customer_signup.html', {'form': form})




# RESTARANT MANAGER SIGNUP


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import ManagerSignUpForm
from .models import RestaurantManager
from restaurant.models import ( 
                     Restaurant, Address )

def restaurant_manager_signup(request):
    if request.method == 'POST':
        form = ManagerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            
            # ایجاد آدرس و رستوران
            address = Address.objects.create(
                street=form.cleaned_data.get('street'),
                city=form.cleaned_data.get('city'),
                state=form.cleaned_data.get('state'),
                zipcode=form.cleaned_data.get('zipcode')
            )
            
            restaurant = Restaurant.objects.create(
                name=form.cleaned_data.get('restaurant_name'),
                address=address,
                manager=user
            )
            
            categories = form.cleaned_data.get('categories')
            restaurant.categories.set(categories)
            restaurant.save()
            
            # اضافه کردن گروه و پرمیشن‌ها
            group, created = Group.objects.get_or_create(name='Restaurant Managers')
            user.groups.add(group)

            login_url = reverse('accounts:login') 
            login_url += f'?next={reverse("accounts:manager_profile", kwargs={"pk": user.pk})}'
            return redirect(login_url)

            # login(request, user)
            # return redirect(reverse('accounts:login'))
    else:
        form = ManagerSignUpForm()
    return render(request, 'accounts/manager_signup.html', {'form': form})

