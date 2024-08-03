from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import *




app_name = 'restaurants-api'




router = DefaultRouter()
router.register(r'address', AddressViewSet, basename='addr')
# router.register(r'restaurant', RestaurantViewSet, basename='rest')
urlpatterns = router.urls


urlpatterns += [
    path('restaurant/list/',  restaurant_list, name='restaurant_list'),
    path('restaurant/<int:id>/',  restaurant_detail, name='restaurant-detail'),
    
    # path('', include('router.urls'))
    # path('address/list/',  address_list, name='address_list'),
    # path('address/<int:id>/',  address_detail, name='address-detail'),
    
    # path('address/',  AddressApiView.as_view(), name='address_list'),
    # path('address/<int:id>/',  AddressDetailApiView.as_view() , name='address-detail'),
    
    # path('address/',  AddressGenericApiView.as_view(), name='address_list'),
    # path('address/<int:id>/',  AddressDetailGenericApiView.as_view() , name='address-detail'),
    
    # path('address/',  AddressViewSet.as_view({'get': 'list', }), name='address_list'),
    # path('address/salam/',  AddressViewSet.as_view({'get':'say_hello'}), name='address_list'),
    # path('address/<int:pk>/',  AddressViewSet.as_view({'get' : 'retrieve', 
    #                                                    'delete': 'destroy'}) , name='address-detail'),
    
]
# urlpatterns += router.urls

