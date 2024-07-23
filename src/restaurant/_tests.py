from django.test import TestCase, SimpleTestCase
from django.urls import reverse , resolve

from .views import (
                    home_page_view, HomePage, 
                    CategoryRestaurantListView,
                    RestaurantDetailView
                )
# Create your tests here.
# assert True == False

from urllib.parse import quote, unquote

class TestUrl(SimpleTestCase):
    
    def test_home_page_url_resolve(self):
        url = reverse('restaurants:home-page-fbv')
        # url = reverse('website:contact')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_page_view)
        
        # url = reverse('restaurants:home-page-cbv')
        # self.assertEquals(resolve(url).func.view_class, HomePage)
        # self.assertEquals(resolve(url).func.view_class, CategoryRestaurantListView)
        
        
    def test_category_restaurant_url_resolve(self):
        
        # url = reverse('restaurants:category-slug-restaurants', kwargs={'slug': 'ایرانی'})
        url = reverse('restaurants:category-slug-restaurants', kwargs={'slug': 'Gilani'})
        self.assertEquals(resolve(url).func.view_class, CategoryRestaurantListView)
        
        slug = 'ایرانی'
        url = reverse('restaurants:category-slug-restaurants', kwargs={'slug': slug})
        decoded_url = unquote(url)
        self.assertEqual(resolve(decoded_url).func.view_class, CategoryRestaurantListView)
        
        
    def test_restaurant_detail(self):
        url = reverse('restaurants:restaurant_detail', kwargs={'pk':1})
        self.assertEquals(resolve(url).func.view_class, RestaurantDetailView)