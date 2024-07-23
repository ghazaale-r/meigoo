from datetime import datetime
from urllib.parse import  unquote, quote

from django.test import TestCase, Client
from django.urls import reverse


from ..models import (
    Restaurant,
    Category,
    Address
)

from accounts.models import User

class TestRestaurantView(TestCase):
    def setUp(self):
        self.client = Client()
        # login required
        self.user_obj = User.objects.create_user(
            email='test2@test.com',
            password='Aa123456#'
        )
        self.addr = Address.objects.create(
            street= 'meidan',
            city='shahr',
            state='ostan'
        )
        
        self.rest = Restaurant.objects.create(
            name = 'test_name', 
            address = self.addr,
            manager= self.user_obj,
            published = datetime.now(), 
            open_close = True, 
            restaurant_parent = None, 
            # categories = [category_obj],
        )
        
        
        self.other_user = User.objects.create_user(
            email='test333@test.com',
            password='Aa123456#'
        )
        
        
    def test_home_page_url_response_200(self):
        url = reverse('restaurants:home-page-fbv')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # print(str(response.content))
        
        # print('===')
        print(str(response.content).find('html'))
        print(str(response.content).find('میگو'))
        # print(str(unquote(response.content)))
        print(str(unquote(response.content)).find('میگو'))
        
        # self.assertTrue(str(response.content).find('میگو'))
        # self.assertTrue(str(unquote(response.content)).find('میگو'))
        self.assertNotEqual(str(unquote(response.content)).find('میگو'), -1)
        self.assertGreaterEqual(str(unquote(response.content)).find('میگو'), 0)
        
        
        
        
    def test_restaurant_detail_logged_in_resposne(self):
        self.client.force_login(self.user_obj)
        url = reverse('restaurants:restaurant_detail', kwargs={'pk':self.rest.id})
        # url = reverse('restaurants:restaurant_detail', kwargs={'pk':1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    
    def test_restaurant_detail_anonymous_response(self):
        url = reverse('restaurants:restaurant_detail', kwargs={'pk':self.rest.id})
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 302)
        
        
    # def test_restaurant_detail_manager_access(self):
    #     self.client.force_login(self.user_obj)
    #     url = reverse('restaurants:restaurant_detail', kwargs={'pk': self.rest.id})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_restaurant_detail_non_manager_access(self):
    #     self.client.force_login(self.other_user)
    #     url = reverse('restaurants:restaurant_detail', kwargs={'pk': self.rest.id})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 403)