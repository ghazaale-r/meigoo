from django.urls import path
from .views import restaurant_page_with_category

urlpatterns = [

    # /category/1/restaurants
    # /category/1
    path('category/<int:category_id>/',  restaurant_page_with_category, name='category-restaurant'),
]
