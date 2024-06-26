from django.urls import path
from .views import *
from django.urls import re_path


app_name = 'restaurants'

urlpatterns = [

    path('',  home_page_view, name='home-page'),
    
    path('category/all/',  category_restaurants_by_name, name='category-restaurants-all'),
    # when slug is english chars a-zA-Z0-9
    # path('category/<slug:slug>/restaurants/',  category_restaurants_by_slug, name='category-slug-restaurants'),
    # when slug is persian or unicode chars
    re_path(r'category/(?P<slug>[\w-]+)/restaurants/$', category_restaurants_by_slug, name='category-slug-restaurants'),

    # path('restaurant/<str:restrnt_name>/menu/',  category_restaurants_by_name, name='category-name-restaurants'),
    path('search/',  search_restaurant, name='search-restaurant'),
    path('test/',  learn_annotate_aggregate, name='test'),
    
]





























from django.urls import path
from .create_restrnt_views import create_address, create_restaurant

urlpatterns += [
    path('create-restaurant/<int:address_id>/', create_restaurant, name='create_restaurant'),
    path('create-restaurant/<int:address_id>/', create_restaurant, name='create_restaurant'),
]