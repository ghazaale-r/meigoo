# import time
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import action
from restaurant.models import Restaurant, Address, Category
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.mixins import (CreateModelMixin, 
                                   ListModelMixin,
                                   RetrieveModelMixin,
                                   UpdateModelMixin,
                                   DestroyModelMixin)

from rest_framework.generics import (GenericAPIView, 
                                    ListCreateAPIView,
                                    RetrieveUpdateDestroyAPIView)
from rest_framework import viewsets

# from ...models import Restaurant

from .serializers import (RestaurantSerializer, RestaurantModelSerializer,
                          AddressModelSerializer,
                          CategoryModelSerializer)

# # @api_view(['GET', 'POST'])
# @api_view()
# def api_restaurant_list(request):
#     # return JsonResponse("ok") #error
#     # return JsonResponse({'name': 'hello'})
#     # return Response("hello")
#     return Response({'name': 'hello'})


@api_view(['GET', 'POST'])
def restaurant_list(request):
    if request.method == 'GET':
        rest_objs = Restaurant.objects.all()
        rest_serial_obj = RestaurantModelSerializer(rest_objs, many=True)
        return Response(rest_serial_obj.data)
    elif request.method == 'POST':
        serializer = RestaurantModelSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    # return Response( {
    #     'status_code': status.HTTP_200_OK,
    #     'data' : rest_serial_obj.data,
    #     'message' : "success"
    # } )




@api_view()
def restaurant_detail(request, id):
    # try:
        rest_obj = get_object_or_404(Restaurant,pk=id)
        # rest_obj = Restaurant.objects.get(pk=id)
        rest_serial_obj = RestaurantSerializer(rest_obj)
        return Response(rest_serial_obj.data)
    # except Restaurant.DoesNotExist:
    #     return Response("rest obj does not exist",status=status.HTTP_404_NOT_FOUND)
        return Response({'detail':"rest obj does not exist" },status=status.HTTP_404_NOT_FOUND)
    
    
    
@api_view(['GET', 'POST'])
def address_list(request):
    if request.method == 'GET':
        serializer = AddressModelSerializer(Address.objects.all(), many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AddressModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAdminUser])
def address_detail(request, id):
    if request.method == 'GET':
        addr_obj = get_object_or_404(Address, pk=id)
        serializer = AddressModelSerializer(addr_obj)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        addr_obj = get_object_or_404(Address, pk=id)
        serializer = AddressModelSerializer(addr_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        addr_obj = get_object_or_404(Address, pk=id)
        addr_obj.delete()
        return Response({
            'detail' : 'address removed successfully'
        }, status=status.HTTP_204_NO_CONTENT)
        
        
        
### class base views
## api view
    
class AddressApiView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = AddressModelSerializer(Address.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = AddressModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class AddressDetailApiView(APIView):
    permission_classes = [IsAdminUser] 
    
    def get(self, request, id):
        addr_obj = get_object_or_404(Address, pk=id)
        serializer = AddressModelSerializer(addr_obj)
        return Response(serializer.data)
    
    def put(self,request, id):
        addr_obj = get_object_or_404(Address, pk=id)
        serializer = AddressModelSerializer(addr_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def patch(self,request, id):
        addr_obj = get_object_or_404(Address, pk=id)
        serializer = AddressModelSerializer(addr_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request, id):
        addr_obj = get_object_or_404(Address, pk=id)
        addr_obj.delete()
        return Response({
            'detail' : 'address removed successfully'
        }, status=status.HTTP_204_NO_CONTENT)
        
        
        
### generics
## genericApiView

class AddressGenericApiView(GenericAPIView,
                            ListModelMixin,
                            CreateModelMixin):
    
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
   
    
class AddressGenericApiView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer

class AddressDetailGenericApiView(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressModelSerializer
    lookup_field = 'id'   

    
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
    
    

    
   
   
### viewset
## viewset
class AddressViewSet(viewsets.ViewSet):

    def list(self, request): # get
        serializer = AddressModelSerializer(Address.objects.all(), many=True)
        return Response(serializer.data)

    @action(methods=['get', 'post'], detail=False)
    def say_hello(self, request):
        return Response({'Hello': 'درود بر شما'})
        
    def create(self, request, pk=None):
        pass
    
    def retrieve(self, request, pk=None): # get 
        addr_obj = get_object_or_404(Address, pk=pk)
        serializer = AddressModelSerializer(addr_obj)
        return Response(serializer.data)

    def put(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass
