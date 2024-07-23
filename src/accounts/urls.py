from django.urls import path
from .views import *
from .sign_up_views import *
from .profile_views import *


app_name = 'accounts'

urlpatterns = [
    # login
    # logout
    # signup / register
    
    path('signup/restaurant_manager/', restaurant_manager_signup, name='restaurant_manager_signup'),
    path('signup/customer/', customer_signup, name='customer_signup'),
    
    
    path('login/', login_view, name='login'), # 127.0.0.1:8000 / accounts / login /
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    
    
    # # mbv
    # path('profile/restaurant_manager/', restaurant_manager_profile, name='restaurant_manager_profile'),
    # path('profile/customer/', customer_profile, name='customer_profile'),
    # cbv
    path('profile/manager/<int:pk>/', ManagerProfileView.as_view(), name='manager_profile'),
    path('profile/customer/<int:pk>/', CustomerProfileView.as_view(), name='customer_profile'),
    # path('profile/restaurant_manager/<int:pk>/restaurants/', ManagerRestaurantListView.as_view(), name='restaurant_list'),
    
    
    path('test/', test, name='test'), # test session / cookie
    
    
]