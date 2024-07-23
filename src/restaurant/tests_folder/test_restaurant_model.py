from datetime import datetime
from django.test import SimpleTestCase, TestCase

from ..models import (
    Restaurant,
    Category,
    Address
)

from accounts.models import User


class TestRestaurantModel(TestCase):
    
    def setUp(self):
        self.user_obj = User.objects.create_user(
            email='test@test.com',
            password='Aa123456#'
        )
        self.category_obj = Category.objects.create(name="hello")
        self.addr_obj = Address.objects.create(
            street= 'meidan',
            city='shahr',
            state='ostan'
        )
    
    def test_create_restaurant_with_valid_data(self):
        # user_obj = User.objects.create_user(
        #     email='test@test.com',
        #     password='Aa123456#'
        # )
        # category_obj = Category.objects.create(name="hello")
        # addr_obj = Address.objects.create(
        #     street= 'meidan',
        #     city='shahr',
        #     state='ostan'
        # )
        
        rest = Restaurant.objects.create(
            name = 'test_name', 
            address = self.addr_obj,
            manager = self.user_obj,
            published = datetime.now(), 
            open_close = True, 
            restaurant_parent = None, 
            # categories = [category_obj],
        )
        # rest.categories.add(category_obj)
        rest.categories.set([self.category_obj])
        
        self.assertEqual(rest.name, 'test_name')
        self.assertTrue(Restaurant.objects.filter(pk=rest.id).exists())
        
        self.assertEqual(rest.categories.get(pk=self.category_obj.pk), self.category_obj)
        self.assertEqual(rest.categories.all()[0], self.category_obj)
        
    