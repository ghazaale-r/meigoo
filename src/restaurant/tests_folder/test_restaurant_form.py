from datetime import datetime
from django.test import SimpleTestCase, TestCase

from ..forms import RestaurantModelForm
from ..models import Category



# class TestRestaurantForm(SimpleTestCase):
class TestRestaurantForm(TestCase):
    
    def test_restaurant_form_with_valid_data(self):
        category_obj = Category.objects.create(name="hello")
        
        form_obj = RestaurantModelForm(data={
            'name': 'test_name', 
            # 'image': , 
            'published': datetime.now(), 
            'open_close': True, 
            'restaurant_parent': None, 
            # 'categories' : [category_obj],
            'categories' : [category_obj],
        })
        # form.is_valid()
        print(form_obj.errors)
        self.assertTrue(form_obj.is_valid())
        
    
    def test_restaurant_form_with_no_data(self):
        form_obj = RestaurantModelForm(data={})
        self.assertFalse(form_obj.is_valid())
        