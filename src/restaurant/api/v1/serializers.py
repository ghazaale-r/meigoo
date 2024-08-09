from django.urls import reverse
from rest_framework import serializers
from restaurant.models import Restaurant, Address, Category
from accounts.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'is_staff', 'is_active']
    
    
class AddressModelSerializer(serializers.ModelSerializer):
    # restaurant_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Address
        fields = "__all__"
        
    # def get_restaurant_url(self, obj):
    #     if obj.pk:
    #         return reverse('restaurants:restaurants-api:res-detail', args=[obj.pk])
    #     else:
    #         return f'/address/{obj.id}/restaurant/'
        
        
        
                
class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'image']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # request 
        # self.request
        # self.get_context().get('request')
        # # list , detail 
        # # ---   , pk 
        
        # representation['message'] = 'درود بر شما'
        # representation['message'] = 'درود بر شما'
        # representation.pop('image')

        return representation


class RestaurantModelSerializer(serializers.ModelSerializer):
    # manager = serializers.SlugRelatedField(
    #     read_only=True,
    #     slug_field='email'
    #  )
    
    # manager = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #  )
    
    # manager = UserModelSerializer()
    name = serializers.CharField(read_only=True)
    id = serializers.ReadOnlyField()
    
    # categories = CategoryModelSerializer(many=True)
    
    # categories = serializers.SlugRelatedField(
    #     read_only=True,
    #     # queryset=Category.objects.all(),
    #     many=True,
    #     slug_field='name'
    # )
    url = serializers.HyperlinkedIdentityField(view_name='restaurants:api-v1:rest-detail')
    address = AddressModelSerializer()
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'open_close',
                  'categories', 'url', 'manager', 'image'
                  ]
        read_only_fields = ['id']
    
        
        
    def create(self, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address_obj = Address.objects.create(**address_data)
        
        # categories = validated_data.pop('categories', None)
        
        rest_obj = Restaurant.objects.create(address=address_obj, **validated_data)
        return rest_obj
        
        
        # # print(categories)
        # # print('=====================')
        # # for cat_data in categories: 
        # #     print(cat_data)
        # #     # print(cat_obj.id, cat_obj.name)
        # #     # created, cat_obj = Category.objects.get_or_create(**cat_data)
        # #     # rest_obj.categories.add(cat_obj)
        
        # print(validated_data)
        
        # return rest_obj
        
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['message'] = 'درود بر شما'

        req = self.context.get('request')
        print(req.__dict__)
        representation['وضعیت'] = 'همه'
        representation['categories'] = CategoryModelSerializer(instance.categories.all(), 
                                                            many=True,
                                                            context={'request': req}).data
        if req.parser_context.get('kwargs').get('pk'):
            representation.pop('realative_url', None)
            representation.pop('abs_url', None)
            representation.pop('url', None)
        # else:
        #      representation.pop('categories', None)
        
        
        

        return representation