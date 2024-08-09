# import time
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes, action
from rest_framework.generics import (GenericAPIView, 
                                    ListCreateAPIView,
                                    RetrieveUpdateDestroyAPIView)
from rest_framework.mixins import (CreateModelMixin, 
                                   ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin)
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView


from restaurant.models import Restaurant, Address, Category
# from ...models import Restaurant

from .serializers import (RestaurantModelSerializer,
                          AddressModelSerializer,
                          CategoryModelSerializer)

# # @api_view(['GET', 'POST'])
# @api_view()
# def api_restaurant_list(request):
#     # return JsonResponse("ok") #error
#     # return JsonResponse({'name': 'hello'})
#     # return Response("hello")
#     return Response({'name': 'hello'})

# DRF :: method base 
# @api_view(['GET', 'POST'])
# def restaurant_list(request):
#     if request.method == 'GET':
#         rest_objs = Restaurant.objects.all()
#         rest_serial_obj = RestaurantModelSerializer(rest_objs, many=True)
#         return Response(rest_serial_obj.data)
#     elif request.method == 'POST':
#         serializer = RestaurantModelSerializer(data=request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

    # return Response( {
    #     'status_code': status.HTTP_200_OK,
    #     'data' : rest_serial_obj.data,
    #     'message' : "success"
    # } )




# @api_view()
# def restaurant_detail(request, id):
#     # try:
#         rest_obj = get_object_or_404(Restaurant,pk=id)
#         # rest_obj = Restaurant.objects.get(pk=id)
#         rest_serial_obj = RestaurantSerializer(rest_obj)
#         return Response(rest_serial_obj.data)
#     # except Restaurant.DoesNotExist:
#     #     return Response("rest obj does not exist",status=status.HTTP_404_NOT_FOUND)
#         return Response({'detail':"rest obj does not exist" },status=status.HTTP_404_NOT_FOUND)
    

# DRF :: method base     
    
# @api_view(['GET', 'POST'])
# def address_list(request):
#     if request.method == 'GET':
#         serializer = AddressModelSerializer(Address.objects.all(), many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = AddressModelSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAdminUser])
# def address_detail(request, id):
#     if request.method == 'GET':
#         addr_obj = get_object_or_404(Address, pk=id)
#         serializer = AddressModelSerializer(addr_obj)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         addr_obj = get_object_or_404(Address, pk=id)
#         serializer = AddressModelSerializer(addr_obj, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         addr_obj = get_object_or_404(Address, pk=id)
#         addr_obj.delete()
#         return Response({
#             'detail' : 'address removed successfully'
#         }, status=status.HTTP_204_NO_CONTENT)
        
        
#### DRF          
### class base views
## api view
    
# class AddressApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         serializer = AddressModelSerializer(Address.objects.all(), many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = AddressModelSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
# class AddressDetailApiView(APIView):
#     permission_classes = [IsAdminUser] 
    
#     def get(self, request, id):
#         addr_obj = get_object_or_404(Address, pk=id)
#         serializer = AddressModelSerializer(addr_obj)
#         return Response(serializer.data)
    
#     def put(self,request, id):
#         addr_obj = get_object_or_404(Address, pk=id)
#         serializer = AddressModelSerializer(addr_obj, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def patch(self,request, id):
#         addr_obj = get_object_or_404(Address, pk=id)
#         serializer = AddressModelSerializer(addr_obj, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request, id):
#         addr_obj = get_object_or_404(Address, pk=id)
#         addr_obj.delete()
#         return Response({
#             'detail' : 'address removed successfully'
#         }, status=status.HTTP_204_NO_CONTENT)
        
        
#### DRF
### generics
## genericApiView

# class AddressGenericApiView(GenericAPIView,
#                             ListModelMixin,
#                             CreateModelMixin):
    
#     queryset = Address.objects.all()
#     serializer_class = AddressModelSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
   
    
# class AddressGenericApiView(ListCreateAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressModelSerializer

# class AddressDetailGenericApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Address.objects.all()
#     serializer_class = AddressModelSerializer
#     lookup_field = 'id'   

    
# class AddressDetailGenericApiView(GenericAPIView,
#                                   RetrieveModelMixin,
#                                   UpdateModelMixin,
#                                   DestroyModelMixin):
#     queryset = Address.objects.all()
#     serializer_class = AddressModelSerializer
#     lookup_field = 'id'
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
    
#     def delete(self,request, *args, **kwargs):
#         return self.destroy(self, request, *args, **kwargs)
    
    
   
#### DRF
### viewset
## viewset

class AddressModelViewSet(viewsets.ModelViewSet):
    
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer
    # permission_classes = [IsAccountAdminOrReadOnly]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        result = {
            'data' : serializer.data,
            'creating_link' : f'address/{serializer.data["id"]}/restaurant/'
                
        }
        return Response(result, status=status.HTTP_201_CREATED, headers=headers)

    
    
    
class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

class RestaurantModelViewSet(viewsets.ModelViewSet):
    # queryset = Restaurant.objects.filter(open_close=True)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantModelSerializer
    # permission_classes = []
    
    def perform_create(self, serializer):
        # serializer.validated_data.pop('manager', None)
        serializer.validated_data['manager'] = self.request.user
        serializer.save()
        
        # cleaned_data
        # inst_obj = form.save(commit=False)
        # inst_obj.manager = self.request.user
        # inst_obj.save() --< model
        
        # m2m
        
        # inst_obj.categories.add(m2m)
        
        