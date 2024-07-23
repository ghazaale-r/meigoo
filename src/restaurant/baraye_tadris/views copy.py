from datetime import datetime, timedelta
from urllib.parse import urljoin

from django.db import connection
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Category, Restaurant




def print_all_categories():
    # یکی از دو خط زیر را از کامنت در بیاورید 
    # با مشکل چندی کویری اگر فیلدی که ریلیشن دارد را صدا بزنید اگر نه که اوکیه 
    # categories_list = Category.objects.all()
    # برای صدا کردن فیلد های ریلیشن دار بهتر است که ابتدا 
    # join
    # زده شود
    categories_list = Category.objects.prefetch_related('restaurants').all()
    
    
    # print(categories_list.query)
    # print('categories_list :' , categories_list)
    for cat in categories_list:
        # print('id :',cat.id)
        # print('image :',cat.image)
        # print('name ',cat.name)
        
        # print(cat.restaurants.all())
        # print(cat.restaurants.all().query)
        # reverse relation m2m , related_name = restaurants
        for cat_restaurant in cat.restaurants.all():
            print(cat_restaurant.name) # اسم رستوران
            

def print_all_restrnts():
    # همانند توضیحات بالا خط ۱۳ تا ۱۸
    # restaurants_list = Restaurant.objects.all()
    restaurants_list = Restaurant.objects.select_related("address").all()

    # restaurants_list = Restaurant.objects.prefetch_related('category').all()
    # print(restaurants_list.query)
    # print('restaurants_list : ', restaurants_list)
    for rest in restaurants_list:
        
        # print('id :',rest.id)
        # print('image :',rest.image)
        # print('image url :',rest.image.url)
        # print('order_count: ',rest.order_count)
        # print('created_at :',rest.created_at)
        # print('open_close :',rest.open_close)
        # print('rating_count :',rest.rating_count)
        # print('average_rating : ',rest.average_rating)
        
        print(" ===== relation fileds ======")
        # print('address :',rest.address)
        # print('restaurant_parent : ',rest.restaurant_parent)
        # if rest.restaurant_parent:
        #     print('restaurant_parent name : ',rest.restaurant_parent.name)
        #     print('restaurant_parent id : ',rest.restaurant_parent.id)
        #     print('restaurant_parent iamge url : ',rest.restaurant_parent.image.url)
        # print('categories :',rest.categories)
        # print('categories all :',rest.categories.all())
        # if rest.categories.all:
        #     print([cat for cat in rest.categories.all()])
        
        print( " ========  methods =======")
        # print('is_main_branch :',rest.is_main_branch())
        # print('get_all_branches :',rest.get_all_branches())
        # print('show_related_branches :',rest.show_related_branches())
        
        print()
        print("-------------------------------------------")
        print()
  
def just_print():
    # print_all_categories()
    print_all_restrnts()
    #  can access in shell
    
    # from djago.db import connections
    queries = connection.queries
    print(len(queries))
    for q in queries:
        print(q)
    

# برای تدریس 
# def home_page_view(request):
#     # just_print()
#     # All the items that should be placed on the homepage.
#     # show all categories
#     # food-party
#     # new resturants 
#         # a week ago
#         # last 10 resturants
#         # aweek ago and just last 10 

#     # show all categories
#     categories_list = Category.objects.all()
#     # print(categories_list)
#     # categories_list = []
    
#     # food-party
#     food_party_flag = False
#     food_party_items = []
    
#     ### new restaurants
    
#     # aweek ago
#     one_week_ago = timezone.now() - timedelta(days=7)
#     # # look up
#     # new_restaurants_from_the_past_week = Restaurant.objects.filter(created_at__gte=one_week_ago)
#     # # last 10 resturants
#     # last_ten_restaurants = Restaurant.objects.order_by('-created_at')[:10]
    
#     # a week ago and up to 10 resturants
#     the_past_week_up_to_the_last_ten_restaurants = Restaurant.objects.filter(created_at__gte=one_week_ago).order_by('-created_at')[:10]
    
#     # دوستان خطوط 132 تا 145 تدریس نشده 
#     # بحث سر تفاوت دو متد 
#     # values    ,    values_list 
#     # هست که در داکیومنت جنگو مثال زده و مثال خروجی هم زده شده 
#     # کلا این دو متد زمانی استفاده میشود که شما نخواهی همه ی فیلد های مدلتان 
#     # یا همان همه ی ستون های جدول را واکشی کنید و ستون های خاصی مد نظرت هست 
    
#     # خودتون زحمت بکشید اجرا کندی و خروجی رو ببینید پرینت خروجی هم کدش نوشته شده است
    
    
#     # recent_restrnts = the_past_week_up_to_the_last_ten_restaurants.values(
#     #                     'name', 'image',
#     #                     'rating_count', 'average_rating', 'categories__name'
#     #                 )
 
#     # # print(' recent_restrnts used --values-- method : ', recent_restrnts)
    
#     # # recent_restrnts = new_restaurants_from_the_past_week.values_list(
#     # #     'name', 'image__url', 
#     # #     'rating_count', 'average_rating', 'categories__name'
#     # # )
#     # # print(' recent_restrnts used --values_list-- method : ', recent_restrnts)
    
#     # #  اگر کدهای بالا رو اجرا کرده باشید متوجه میشود که صدا زدن 
#     # # image_url
#     # # اشتباه هست 
    
#     # # print(recent_restrnts[0]['image'].url) # error str obj has no url
#     # # import
#     # # from django.conf import settings
#     # # from urllib.parse import urljoin
    
#     # # # # Base URL for media files
#     # media_url = settings.MEDIA_URL
#     # # # print(urljoin(media_url, recent_restrnts[0]['image']) if recent_restrnts[0]['image'] else None,)
       
#     # for rest in recent_restrnts:
#     #     rest['image'] = urljoin(media_url, rest['image']) if rest['image'] else None


#     recent_restrnts = the_past_week_up_to_the_last_ten_restaurants.prefetch_related(
#                         'categories'
#                     )
    
#     media_url = settings.MEDIA_URL
    
  
#     context = {
#         'categories' : categories_list,
        
#         'food_party_flag' : food_party_flag,
#         'food_party_iitems' : food_party_items,
        
#         'recent_restaurants': recent_restrnts
#         # 'recent_restaurants': processed_restaurants
#     }
    
#     return render(request, 'restaurant/home_page.html', context)
    




def home_page_view(request):
    # show all categories
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
        'categories' : categories_list,
        
        'food_party_flag' : food_party_flag,
        'food_party_iitems' : food_party_items,
        
        'recent_restaurants': recent_restrnts
        # 'recent_restaurants': processed_restaurants
    }
    
    return render(request, 'restaurant/home_page.html', context)





# def category_restaurants_by_id(request, category_id=None):
#     print('category_id :', category_id)
#     categories_list = Category.objects.all()
    
    
#     selected_category = None
#     category_restrnt = Restaurant.objects.all()
    
    
#     if category_id:
#         # selected_category = Category.objects.filter(id=category_id)
#         # selected_category.restaurants
#         selected_category = Category.objects.prefetch_related('restaurants').filter(id=category_id)
#         print(selected_category) # حواستون باشه که این لیست هست از یک کتگوری انتخاب شده
#         # طریقه ی دسترسی به رستوران های کتگوری انتخاب شده 
#         print(selected_category[0].restaurants.all())
#         # selected_category.restarants
#         # selected_category.restarants.name
#         # selected_category.restarants.image
        
        
#         category_restrnt = Restaurant.objects.filter(categories__id=category_id)
    
#     context = {
#         'categories' : categories_list,
#         'selected_category' : selected_category,
#         # 'selected_category' : [selected_category] if category_id else selected_category,
#         # 'category_restrnt' : category_restrnt,
#         'category_flag': 'id'
        
#     }
    
#     return render(request, 'restaurant/categories_restaurants_page.html', context)




def category_restaurants_by_name(request, category_name=None):
    print('category_name :', category_name)
    categories_list = Category.objects.all()
    category_restrnt = Restaurant.objects.all()
    
    if category_name :
        # category_restrnt = Restaurant.objects.filter(categories__name__contains=category_name)
        category_restrnt = Restaurant.objects.prefetch_related('categories').filter(categories__name__contains=category_name)
   
    context = {
        'categories' : categories_list,
        # 'selected_category' : selected_category,
        'category_restrnt' : category_restrnt,
        'category_flag': 'name'
    }
    
    return render(request, 'restaurant/categories_restaurants_page.html', context)



# صرفا برای اینکه بدونید برای چه ریلیشنی از کدوم متد استفاده کنید
# فرض کنید می‌خواهید تمام رستوران‌ها را با تمام روابط مرتبط آن‌ها دریافت کنید
# حتما توی django-debug toolbar 
# برید و کویری را ببینید 
# البته باید این تکه کد را درون یک متد ویو کپی کند
# برای راحتی در متد home_page 
# کپی کنید
# restaurants = Restaurant.objects.select_related(
#     'address',                # OneToOneField
#     'restaurant_parent'       # ForeignKey one2many
# ).prefetch_related(
#     'categories',             # ManyToManyField
#     'branches',               # Reverse ForeignKey (related_name)
#     'menu_set',               # Reverse ForeignKey (default related_name)
#     'rating_set'              # Reverse ForeignKey (default related_name)
# ).all()


# همون قسمتی که گفتم تدریس نشده از خط ۱۳۲ تا ۱۴۵ رو برای این کویری هم اعمال کردم 
# تا متوجه بشید برای دسترسی به فیلد از یک فیلدی که ریلیشن دارد جطور باید کد بزنید
# مثلا فیلد شهر از جدول ادرس که با جدول رستوران ریلیشن دارد

# restaurants = Restaurant.objects.select_related(
#     'address',                # OneToOneField
#     'restaurant_parent'       # ForeignKey
# ).prefetch_related(
#     'categories',             # ManyTفoManyField
#     'branches',               # Reverse ForeignKey (related_name)
#     'menu_set',               # Reverse ForeignKey (default related_name)
#     'rating_set'              # Reverse ForeignKey (default related_name)
# ).values('name', 'address__city', 'categories__name', 'rating_count')

# for restaurant in restaurants:
#     print(f"Restaurant Name: {restaurant['name']}, City: {restaurant['address__city']}, Category: {restaurant['categories__name']}, Ratings: {restaurant['rating_count']}")
    
    
# .values_list('name', 'address__city', 'categories__name')

# for name, city, category in restaurants:
#     print(f"Restaurant Name: {name}, City: {city}, Category: {category}")