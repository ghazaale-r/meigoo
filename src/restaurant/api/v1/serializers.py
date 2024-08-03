from rest_framework import serializers

from restaurant.models import Restaurant, Address, Category



class AddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        
        
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"



class RestaurantSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    # manager = serializers.IntegerField()
    name = serializers.CharField()
    image = serializers.ImageField()
    

class RestaurantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['manager', 'name', 'address', 'open_close', 'average_rating']