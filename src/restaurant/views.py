from django.utils import timezone
from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404

from .models import Category, Restaurant

from django.db import connection



def print_all_categories():
    pass
    # categories_list = Category.objects.all()
    # categories_list = Category.objects.prefetch_related('restaurants').all()
    # print(categories_list.query)
    # print('categories_list :' , categories_list)
    # for cat in categories_list:
    #     print('id :',cat.id)
    #     print('image :',cat.image)
    #     print('name ',cat.name)
    #     print('name ',cat.name)
    #     # print(cat.restaurants.all())
    #     # for cat_r in cat.restaurants.all():
    #     #     print(cat_r.name)
    #     print("================================================")

def print_all_restrnts():
    restaurants_list = Restaurant.objects.all()
    restaurants_list = Restaurant.objects.prefetch_related('category').all()
    print(restaurants_list.query)
    print('restaurants_list : ', restaurants_list)
    for rest in restaurants_list:
        
        print('id :',rest.id)
        print('image :',rest.image)
        print('image url :',rest.image.url)
        print('order_count: ',rest.order_count)
        print('created_at :',rest.created_at)
        print('open_close :',rest.open_close)
        print('rating_count :',rest.rating_count)
        print('average_rating : ',rest.average_rating)
        
        print(" ===== relation fileds ======")
        print('address :',rest.address)
        print('restaurant_parent : ',rest.restaurant_parent)
        if rest.restaurant_parent:
            print('restaurant_parent name : ',rest.restaurant_parent.name)
            print('restaurant_parent id : ',rest.restaurant_parent.id)
            print('restaurant_parent iamge url : ',rest.restaurant_parent.image.url)
        print('categories :',rest.categories)
        print('categories all :',rest.categories.all())
        if rest.categories.all:
            print([cat for cat in rest.categories.all()])
        
        print( " ========  mthods =======")
        print('is_main_branch :',rest.is_main_branch())
        print('get_all_branches :',rest.get_all_branches())
        print('show_related_branches :',rest.show_related_branches())
        
        print()
        print("-------------------------------------------")
        print()

    
def just_print():
    print_all_categories()
    # print_all_restrnts()
    
    queries = connection.queries
    print(len(queries))
    for q in queries:
        print(q)
    

def home_page_view(request):
    just_print()
    # All the items that should be placed on the homepage.
    # show all categories
    # food-party
    # new resturants 
        # a week ago
        # last 10 resturants
        # aweek ago and just last 10 

    # show all categories
    # categories_list = Category.objects.all()
    categories_list = []
    
    # food-party
    foos_party_flag = False
    food_party_items = []
    
    ### new restaurants
    
    # aweek ago
    one_week_ago = timezone.now() - timedelta(days=7)
    new_restaurants_from_the_past_week = Restaurant.objects.filter(created_at__gte=one_week_ago)
    
    # last 10 resturants
    # last_ten_restaurants = Restaurant.objects.order_by('-created_at')[:10]
    
    # a week ago and up to 10 resturants
    # the_past_week_up_to_the_last_ten_restaurants = Restaurant.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')[:10]
    
    # recent_restrnts = new_restaurants_from_the_past_week.values(
    #     'name', 'image__url', 
    #     'rating_count', 'average_rating', 'categories__name'
    # )
    
    # recent_restrnts = new_restaurants_from_the_past_week.values_list(
    #     'name', 'image__url', 
    #     'rating_count', 'average_rating', 'categories__name'
    # )
    
    # for r in recent_restrnts:
    #     print(r)
        
        
    context = {
        'categories' : categories_list,
        'foos_party_flag' : True,
        'food_party_iitems' : [],
        'new_restaurants_from_the_past_week': [],
        'last_ten_restaurants': [],
        'recent_restaurants': recent_restrnts
    }
    return render(request, 'restaurant/home_page.html', context)
    


def category_restaurants_by_id(request, category_id=None):
    print('category_id :', category_id)
    categories_list = Category.objects.all()
    selected_category = None
    category_restrnt = Restaurant.objects.all()
    if category_id:
        selected_category = Category.objects.filter(id=category_id)
        category_restrnt = Restaurant.objects.filter(categories__id=category_id)
    
    context = {
        'categories' : categories_list,
        'selected_category' : selected_category,
        # 'selected_category' : [selected_category] if category_id else selected_category,
        'category_restrnt' : category_restrnt,
        'category_flag': 'id'
        
    }
    
    return render(request, 'restaurant/categories_restaurants_page.html', context)




def category_restaurants_by_name(request, category_name=None):
    print('category_name :', category_name)
    categories_list = Category.objects.all()
    category_restrnt = Restaurant.objects.all()
    if category_name:
        # category_restrnt = Restaurant.objects.filter(categories__name__contains=category_name)
        category_restrnt = Restaurant.objects.prefetch_related('categories').filter(categories__name__contains=category_name)
   
    context = {
        'categories' : categories_list,
        # 'selected_category' : selected_category,
        'category_restrnt' : category_restrnt,
        'category_flag': 'name'
    }
    
    return render(request, 'restaurant/categories_restaurants_page.html', context)




# فرض کنید می‌خواهید تمام رستوران‌ها را با تمام روابط مرتبط آن‌ها دریافت کنید
restaurants = Restaurant.objects.select_related(
    'address',                # OneToOneField
    'restaurant_parent'       # ForeignKey
).prefetch_related(
    'categories',             # ManyToManyField
    'branches',               # Reverse ForeignKey (related_name)
    'menu_set',               # Reverse ForeignKey (default related_name)
    'rating_set'              # Reverse ForeignKey (default related_name)
).all()



restaurants = Restaurant.objects.select_related(
    'address',                # OneToOneField
    'restaurant_parent'       # ForeignKey
).prefetch_related(
    'categories',             # ManyToManyField
    'branches',               # Reverse ForeignKey (related_name)
    'menu_set',               # Reverse ForeignKey (default related_name)
    'rating_set'              # Reverse ForeignKey (default related_name)
).values('name', 'address__city', 'categories__name', 'rating_count')

for restaurant in restaurants:
    print(f"Restaurant Name: {restaurant['name']}, City: {restaurant['address__city']}, Category: {restaurant['categories__name']}, Ratings: {restaurant['rating_count']}")
    
    
# .values_list('name', 'address__city', 'categories__name')

# for name, city, category in restaurants:
#     print(f"Restaurant Name: {name}, City: {city}, Category: {category}")