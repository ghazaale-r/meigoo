from django.urls import path
from .views import *

app_name = 'restaurants'

urlpatterns = [

    path('',  home_page_view, name='home-page'),
    
    path('category/all/',  category_restaurants_by_name, name='category-restaurants-all'),
    path('category/<str:category_name>/restaurants/',  category_restaurants_by_name, name='category-name-restaurants'),
    
    # path('restaurant/<str:restrnt_name>/menu/',  category_restaurants_by_name, name='category-name-restaurants'),
    path('search/',  search_restaurant, name='search-restaurant'),
    
]
