from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # login
    # logout
    # signup / register
    
    path('login/', login_view, name='login'), # 127.0.0.1:8000 / accounts / login /
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
    
    path('test/', test, name='test'), # test session / cookie
]
