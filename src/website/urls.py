from django.urls import path
from .views import *


app_name = 'website'

urlpatterns = [
    path('contact/',  contact_page, name="contact"),
    path('test/form/',  test_form_view, name='test-form'),
]