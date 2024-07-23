from datetime import datetime, timedelta
from urllib.parse import urljoin



from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.utils.decorators import method_decorator
from django.views import View
# class based views
from django.views.generic import (
                            ListView,
                            DetailView,
                            CreateView,
                            UpdateView,
                            DeleteView
                                  )
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Restaurant
from .forms import RestaurantModelForm


from django.template.response import TemplateResponse




from django.http import HttpResponse
from django.utils.decorators import decorator_from_middleware
from website.middlewares import custom_middleware
custom_middleware = decorator_from_middleware(custom_middleware.CustomMiddleware)

@custom_middleware
def example_view(request, id, slug):
    return HttpResponse(f'ID: {id}, Slug: {slug}')


# class Salam(View):
#     @custom_middleware
#     def get(self, request, id, slug):
#         return HttpResponse(f'ID: {id}, Slug: {slug}')
    
# @method_decorator(custom_middleware, name='dispatch')
# class Salam(View):
#     def get(self, request, id, slug):
#         return HttpResponse(f'ID: {id}, Slug: {slug}')



# @login_required
def home_page_view(request):
    # show all categoriesج
    categories_list = Category.objects.all()
    
    # food-party
    food_party_flag = False
    food_party_items = []
    
    ### new restaurants
    # aweek ago
    one_week_ago = timezone.now() - timedelta(days=7)
    # a week ago and up to 10 resturants
    the_past_week_up_to_the_last_ten_restaurants = Restaurant.objects.filter(
                                    created_at__gte=one_week_ago).order_by(
                                    '-created_at').prefetch_related(
                                    'categories'
                                    )[:10]
    
  
    recent_restrnts = the_past_week_up_to_the_last_ten_restaurants    
  
    context = {
        'cats' : categories_list,
        
        'food_party_flag' : food_party_flag,
        'food_party_iitems' : food_party_items,
        
        'recent_restaurants': recent_restrnts
    }
    
    return TemplateResponse(request, 'restaurant/home_page.html', context)
    # return render(request, 'restaurant/home_page.html', context)




class HomePage(View):
    def get(self, request, *args, **kwargs):
        # show all categoriesج
        categories_list = Category.objects.all()
        
        # food-party
        food_party_flag = False
        food_party_items = []
        
        ### new restaurants
        # aweek ago
        one_week_ago = timezone.now() - timedelta(days=7)
        # a week ago and up to 10 resturants
        the_past_week_up_to_the_last_ten_restaurants = Restaurant.objects.filter(
                                        created_at__gte=one_week_ago).order_by(
                                        '-created_at').prefetch_related(
                                        'categories'
                                        )[:10]
        
    
        recent_restrnts = the_past_week_up_to_the_last_ten_restaurants    
    
        context = {
            'cats' : categories_list,
            
            'food_party_flag' : food_party_flag,
            'food_party_iitems' : food_party_items,
            
            'recent_restaurants': recent_restrnts
        }
    
        return render(request, 'restaurant/home_page.html', context)












# @login_required
# def category_restaurants_by_name(request, category_name=None):
#     print('category_name :', category_name)
#     categories_list = Category.objects.all()
#     category_restrnt = Restaurant.objects.all()
    
#     if category_name :
#         category_restrnt = Restaurant.objects.prefetch_related('categories').filter(categories__name__contains=category_name)
   
#     # from_view_1 = True
#     # if category_restrnt:
#     #     from_view_1 = False
    
        
#     context = {
#         'categories' : categories_list,
#         'category_restrnt' : category_restrnt,
#         'category_flag': 'name',
#         # 'from_view_1' : from_view_1
#         'msg_not_found' : 'هیچ رستورانی دراین دسته بندی وجود ندارد'
#     }
    
#     return render(request, 'restaurant/categories_restaurants_page.html', context)


# def category_restaurants_by_slug(request, slug=None):
#     print('slug :', slug)
#     categories_list = Category.objects.all()
#     category_restrnt = Restaurant.objects.all()
    
#     if slug :
#         category_restrnt = Restaurant.objects.prefetch_related('categories').filter(categories__slug__icontains=slug)
   
#     context = {
#         'categories' : categories_list,
#         'category_restrnt' : category_restrnt,
#         'category_flag': 'name',
#         'msg_not_found' : 'هیچ رستورانی دراین دسته بندی وجود ندارد'
#     }
    
#     return render(request, 'restaurant/categories_restaurants_page.html', context)

class CategoryRestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant/categories_restaurants_page.html'
    context_object_name = 'category_restrnt'

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        if category_slug == 'all':
            return Restaurant.objects.all()
        elif category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            return Restaurant.objects.filter(categories=self.category)
        return Restaurant.objects.none()

    def get_context_data(self, **kwargs):
        category_slug = self.kwargs.get('slug')
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if category_slug == 'all':
            context['msg_not_found'] = 'هیچ رستورانی وجود ندارد'
        else:
            context['msg_not_found'] = 'هیچ رستورانی دراین دسته بندی وجود ندارد'
        return context








# def search_restaurant(request):
#     # import pprint
#     # pprint.pprint(request.__dict__)
#     # print(request.method)
#     print(request.GET) 
#     # print(request.GET.get('q')) 
    
#     restaurants = []
#     if request.method == 'GET':
#         restaurant_name = request.GET.get('q')
#         restaurants = Restaurant.objects.filter(name__contains=restaurant_name)
#     categories_list = Category.objects.all()
    
#     from_view_2 = True
#     if restaurants:
#         from_view_2 = False
        
#     context = {
#         'category_restrnt' : restaurants,
#         'categories' : categories_list,
#         # 'from_view_2' : from_view_2,
#         'msg_not_found': f'رستورانی بنام {restaurant_name}  وجود ندارد'
#         # 'rest_name' : restaurant_name
#     }
    
#     return render(request, 'restaurant/categories_restaurants_page.html', context)



class RestaurantSearchListView(ListView):
    model = Restaurant
    template_name = 'restaurant/categories_restaurants_page.html'
    context_object_name = 'category_restrnt'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Restaurant.objects.filter(name__icontains=query)
        return Restaurant.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        q = self.request.GET.get('q', '')
        context['msg_not_found'] =  f'رستورانی بنام {q}  وجود ندارد'
        return context


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin


class RestaurantDetailView(LoginRequiredMixin, UserPassesTestMixin,  DetailView):
# class RestaurantDetailView(LoginRequiredMixin, DetailView):
    # permission_required = 'restaurant.view_restaurant'
    model = Restaurant
    template_name = 'restaurant/restaurant_detail.html'
    context_object_name = 'restaurant'
    
    def test_func(self):
        # rest_obj = Restaurant.objects.filter(user=self.request.user)
        self.object = self.get_object()
        return self.request.user == self.object.manager
    
class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
    model = Restaurant
    form_class = RestaurantModelForm
    template_name = 'restaurant/restaurant_edit.html'

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)
    



















# from django.http import HttpResponse
# from django.db.models import Avg, Count, Min, Max, Sum
# def learn_annotate_aggregate(request):
    
#     # استفاده از 
#     # annotate
#     # برای اضافه کردن میانگین تعداد بازدید به هر کتگوری
#     categories = Category.objects.annotate(avg_views=Avg('restaurants__count_view'))
    
#     for category in categories:
#         print(category.restaurants.all())
#         print(f"Category: {category.name}, Average Views: {category.avg_views}")
        
#     categories = Category.objects.annotate(total_views=Sum('restaurants__count_view'))
#     for category in categories:
#         print(f"Category: {category.name}, Total Views: {category.total_views}")
            
#     ress = Restaurant.objects.aggregate(min_order=Min("order_count"), max_price=Max("order_count"))
#     print(ress)
        
#     return HttpResponse('salam')
