from django.urls import path, re_path, include

from .views import *


app_name = 'restaurants'


urlpatterns = [
    path('',  HomePage.as_view(), name='home-page-cbv'),
    re_path(r'category/(?P<slug>[\w\u0600-\u06FF-]+)/restaurants/$', 
            CategoryRestaurantListView.as_view(), name='category-slug-restaurants'),

    path('search/',  RestaurantSearchListView.as_view(), name='search-restaurant'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('restaurant/<int:pk>/edit/', RestaurantUpdateView.as_view(), name='restaurant_update'),
    
    
    # path('restaurant/', api_restaurant_list, name='restaurant-list'),
    path('api/v1/', include('restaurant.api.v1.urls')),

    
]




from .manager_views import *

urlpatterns += [
    path('address/create/', AddressCreateView.as_view(), name='add_address'),
    path('restaurant/<int:address_id>/create/', RestaurantCreateView.as_view(), name='create_restaurant'),
]