

from django.views import View
# class based views
from django.views.generic import (
                            ListView,
                            DetailView,
                            CreateView,
                            UpdateView,
                            DeleteView
                                  )
from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import *
from .models import Address, Restaurant


#  step 1 use form

def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            # ایجاد شی‌ء آدرس جدید و ذخیره آن در پایگاه داده
            Address.objects.create(
                street=form.cleaned_data['street'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zip_code=form.cleaned_data['zip_code']
            )
            # هدایت کاربر به صفحه ایجاد رستوران
            return redirect(reverse('create_restaurant', args=[new_address.id])) # فرض بر این است که URL مناسب تنظیم شده است
    else:
        form = AddressForm()

    return render(request, 'manager/creation/create_address.html', {'form': form})



def create_restaurant(request, address_id):
    address = Address.objects.get(id=address_id) 
    
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            # Create Restaurant instance from form data
            restaurant = Restaurant()
            restaurant.name = form.cleaned_data['name']
            restaurant.slug = form.cleaned_data['slug'] if form.cleaned_data['slug'] else form.cleaned_data['name']
            restaurant.address = Address.objects.get(pk=form.cleaned_data['address'])
            new_restaurant.address = address
            restaurant.image = form.cleaned_data['image']
            restaurant.open_close = form.cleaned_data['open_close']
            restaurant.average_rating = form.cleaned_data['average_rating']
            
            # Handle restaurant parent (optional)
            if form.cleaned_data['restaurant_parent']:
                restaurant.restaurant_parent = Restaurant.objects.get(pk=form.cleaned_data['restaurant_parent'])

            restaurant.save()

            category_ids = form.cleaned_data['categories']
            for cat_id in category_ids:
                cat = Category.objects.get(pk=cat_id)
                restaurant.categories.add(cat)
            
            return redirect(reverse('restaurants:category-slug-restaurants'))
    else:
        form = RestaurantForm()

    return render(request, 'manager/creation/create_restaurant.html', {'form': form})






# step 2 use model form

def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            # Redirect to the restaurant creation page, passing the address ID
            return redirect('restaurants:create_restaurant', address_id=address.pk)
    else:
        form = AddressForm()

    return render(request, 'manager/creation/create_address.html', {'form': form})




def create_restaurant(request, address_id):
    if request.method == 'POST':
        form = RestaurantForm(request.POST, request.FILES, address_id=address_id)
        if form.is_valid():
            form.save()
            return redirect(reverse('restaurants:category-slug-restaurants')) # Redirect to the list of restaurants or any other appropriate view
    else:
        form = RestaurantForm(address_id=address_id)

    return render(request, 'manager/creation/create_restaurant.html', {'form': form})










# step 3 use CBV and modelforms

class AddressCreateView(CreateView):
    model = Address
    form_class = AddressModelForm
    template_name = 'manager/creation/create_address.html'

    def form_valid(self, form):
        self.object = form.save()
        return redirect(reverse('restaurants:create_restaurant', kwargs={'address_id': self.object.id}))




class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantModelForm
    template_name = 'manager/creation/create_restaurant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = get_object_or_404(Address, id=self.kwargs['address_id'])
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.address = get_object_or_404(Address, id=self.kwargs['address_id'])
        self.object.save()
        form.save_m2m()
        return redirect(reverse('restaurants:restaurant_detail', kwargs={'pk': self.object.pk}))















