from django.urls import path, re_path
from .views import *

from django.views.generic import TemplateView, RedirectView


app_name = 'website'


urlpatterns = [
    path('contact/',  contact_page, name="contact"),
    
    
    
    path('cbv/',  MyView.as_view(), name="cbv"),
    
    
    
    
    
    
    
    
    
    
    path('index/f/',  index_f_view, name='index-f'),
    # use TemplateView directy
    # path('index/c/',  TemplateView.as_view(template_name="index.html"), name='index-c'),
    path('index/c/',  IndexTemplateView.as_view(), name='index-c'),
    
    
    
    
    
    # path('index/c/',  TemplateView.as_view(
    #     template_name="index.html",extra_context = {'name':'ali'}), name='index-c'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # path('index/c/<int:pk>',  IndexTemplateView.as_view(), name='index-c'),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path("go-to-django/",
        RedirectView.as_view(url="https://www.djangoproject.com/"),
        name="go-to-django",
    ),
    
    
    
    
    
    
    path("go-to-index/",
        RedirectView.as_view(pattern_name="website:index-c"),
        name="go-to-index",
    ),
    
    
    
    
    
    path("landing/page/",
        RedirectView.as_view(pattern_name="restaurants:home-page"),
        name="go-to-home-page",
    ),
    
    
    
    
    path("go-to-article/<int:pk>/",
        RedirectView.as_view(pattern_name="restaurants:home-page"),
        name="go-to-home-page",
    ),
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    path('category/',  CategoryListView.as_view(), name='category-list'),
    # path('category/<int:id>/',  CategoryDetailView.as_view(), name='category-detail'),
    # path('category/<int:pk>/',  CategoryDetailView.as_view(), name='category-detail'),
    path('category/<str:slug>',  CategoryDetailView.as_view(), name='category-detail'),
    # re_path(r'category/(?P<slug>[\w\d*-]+)/$', 
    #         CategoryDetailView.as_view(), name='category-slug-restaurants'),
    # path('category/create/form',  CategoryFormView.as_view(), name='category-create'),
    path('contact/create/',  ContactFormView.as_view(), name='contact-create'),

    path('category/create/',  CategoryCreateView.as_view(), name='category-create'),
    
    path('category/<int:pk>/edit/',  CategoryUpdateView.as_view(), name='category-edit'),
    
    path('category/<int:pk>/delete/',  CategoryDeleteView.as_view(), name='category-del'),
    
    
]