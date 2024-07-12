from django.urls import path, re_path

from .views import *


app_name = 'restaurants'


urlpatterns = [
    # path('example/<int:id>/<str:slug>/', example_view, name='example'),
    path('example/<int:id>/<str:slug>/', Salam.as_view(), name='example'),
    
    
    path('',  home_page_view, name='home-page'),
    # path('',  home_page.as_view(), name='home-page'),
    
    # path('category/all/',  category_restaurants_by_name, name='category-restaurants-all'),
    # when slug is english chars a-zA-Z0-9
    # path('category/<slug:slug>/restaurants/',  category_restaurants_by_slug, name='category-slug-restaurants'),
    # when slug is persian or unicode chars
    # re_path(r'category/(?P<slug>[\w-]+)/restaurants/$', category_restaurants_by_slug, name='category-slug-restaurants'),
    re_path(r'category/(?P<slug>\w+)/restaurants/$', 
            CategoryRestaurantListView.as_view(), name='category-slug-restaurants'),

    # path('restaurant/<str:restrnt_name>/menu/',  category_restaurants_by_name, name='category-name-restaurants'),
    # path('search/',  search_restaurant, name='search-restaurant'),
    path('search/',  RestaurantSearchListView.as_view(), name='search-restaurant'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurant/<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_update'),
    
    # path('test/',  learn_annotate_aggregate, name='test'),
    
]




from django.urls import path
from .manager_views import *

urlpatterns += [
    # path('address/create/', create_address, name='add_address'),
    # path('restaurant/<int:address_id>/create/', create_restaurant, name='create_restaurant'),
    
    path('address/create/', AddressCreateView.as_view(), name='add_address'),
    path('restaurant/<int:address_id>/create/', RestaurantCreateView.as_view(), name='create_restaurant'),
]