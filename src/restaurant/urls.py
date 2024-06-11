from django.urls import path
from .views import test_home_page

urlpatterns = [

    path('',  test_home_page),
    # path('',  test_home_page),
]
