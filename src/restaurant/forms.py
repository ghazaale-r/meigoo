
    
from .models import Restaurant, Category, Address



from django import forms




class AddressForm(forms.Form):
    street = forms.CharField(label='خیابان', max_length=255)
    city = forms.CharField(label='شهر', max_length=100)
    state = forms.CharField(label='استان', max_length=100)
    zipcode = forms.CharField(label='کد پستی', max_length=10)
    
    
class AddressModelForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'zipcode']
        labels = {
            "street": 'خیابان',
            "city": 'شهر',
            "satate": 'استان',
            "zipcode": 'کد پستی',
        }
    
    
    

class RestaurantForm(forms.Form):
    name = forms.CharField(max_length=100)
    slug = forms.CharField(max_length=100, required=False)
    address = forms.IntegerField()  #  address ID
    image = forms.ImageField(required=False)
    open_close = forms.BooleanField(required=False)
    restaurant_parent = forms.IntegerField(required=False)  #  restaurant parent ID 
    categories = forms.MultipleChoiceField(choices=[], required=False)  # در متد زیر هنگام ایجاد لیست کتگوری ها رو ایجاد میکنیم 
    
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        from .models import Category  # Import here to avoid circular imports
        self.fields['categories'].choices = [(cat.id, cat.name) for cat in Category.objects.all()]










        
    
class RestaurantModelForm(forms.ModelForm):
    # categories = forms.ModelMultipleChoiceField(
    #     queryset=Category.objects.all(),
    #     widget=forms.SelectMultiple,  # or forms.Select for single selection
    #     required=False
    # )
    
    # published = forms.DateField(
    #     widget=forms.DateInput(format='%Y-%m-%d'),
    #     input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    # )
    
    class Meta:
        model = Restaurant
        fields = ['name', 'image', 
                  'published', 'open_close', 
                  'restaurant_parent', 'categories']
        
        labels = {
            "name": 'نام رستوران',
            "address": 'آدرس',
            "image": 'عکس ',
            "published": 'زمان انتشار ',
            "open_close": ' باز است؟',
            "restaurant_parent": 'شعبه اصلی ',
            "categories": 'دسته بندی ها',
        }
        
        help_texts = {
            "published": "yyyy-mm-dd",
        }
        
        error_messages = {
            "name": {
                "max_length": "This writer's name is too long.",
            },
        }
        widgets = {
            'published': forms.DateInput(attrs={'type': 'date'}),
            # 'published': forms.TimeInput(attrs={'type': 'time'}),
            # "published": forms.DateTimeInput(attrs={'type': 'datetime-local'})
            # 'categories': forms.CheckboxSelectMultiple,
        }








from django import forms
from .models import Restaurant, Address

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'image', 'open_close', 'restaurant_parent', 'categories']

    def __init__(self, *args, **kwargs):
        self.address_id = kwargs.pop('address_id', None)
        print(self.address_id)
        super(RestaurantForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        restaurant = super().save(commit=False)
        if self.address_id:
            restaurant.address = Address.objects.get(pk=self.address_id)
        if commit:
            restaurant.save()
            self.save_m2m()
        return restaurant

