from datetime import datetime
from unidecode import unidecode 

# from django.contrib.auth.models import User
from django.core.validators import ( MinLengthValidator, MaxLengthValidator,
                                        MinValueValidator, MaxValueValidator)
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.text import slugify

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
# sql "create table restaurant (name text, ...")

class Address(models.Model):
    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10, blank=True,
                               validators=[
                                   MinLengthValidator(10),
                                    MaxLengthValidator(10)
                               ])

    def __str__(self):
        return f"{self.id} {self.state}, {self.city}, {self.street}"
    
    
        
        
class Category(models.Model):
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
    # id 
    name = models.CharField(max_length=100, unique=True)
    # فیلد slug از روی فیلد نام ایجاد میشود
    # وچون بنا هست که در url استفاده شود پس باید یونیک باشد در نتیجه ما فیلد نام را نیز یونیک کردیم
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True, allow_unicode=True)
    
    


    image = models.ImageField(upload_to='categories_images/', blank=True, null=True, default='cat-default.jpg')
    # restaurants = sdfkj
    # def restaurant_image_upload_to(instance, filename):
    #     # filename = 'skdfhkj.jpg'
    #     filename = f'{instance.id}-{filename}' if instance.id else filename
    #     return f'cats_im/{datetime.now().strftime("%Y-%m/")}/{filename}'
    # image_22 = models.ImageField(upload_to ='cats_img/%Y/%m/%d/', default='default.jpg') 
    # image_33 = models.ImageField(upload_to =restaurant_image_upload_to, blank=True, null=True)
    # restaurants = این رو برو وصل کن به رستوران ها

    
    def __str__(self):
        return self.name
    
    
    def save(self, *args, **kwargs):
        print('================================')
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)
        


class Restaurant(models.Model):
    class Meta:
        ordering = ["updated_at"]
        verbose_name = "رستوران"
        verbose_name_plural = "رستوران ها"

    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True, blank=True, allow_unicode=True)
    
    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    
    image = models.ImageField(upload_to ='restaurants_imgs/%Y/%m/', default='restrnt-default.jpg') 
     
    order_count = models.IntegerField(default=0)
    count_view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True, blank=True)
    
    open_close = models.BooleanField(null=True, blank=True)
    # open_close = models.NullBooleanField()
    
    restaurant_parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.DO_NOTHING, related_name='branches')
    categories = models.ManyToManyField(Category, related_name='restaurants')
    # rating ...
    rating_count = models.IntegerField(default=0)
    sum_rating = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=2, decimal_places=1, 
                                        default=1.0,
                                        validators=[
                                            MinValueValidator(1.0), 
                                            MaxValueValidator(5.0)
                                        ])
    # main_branch = models.BooleanField(default=False, null=False)


    def save(self, *args, **kwargs):
        # فیلد اسلاگ باید یونیک باشد پس چون اسلاگ از روی نام رستوران هست و ما فیلد نام را یونیک نکرده ایم
        # برخلاف فیلد نام کتگوری که یونیک کرده ایم 
        # باید هنگام ذخیره ابجکت رستوران که اسلاگ را نیز ایجاد میکنیم 
        # باید چک کنیم ان اسلاگ برای رستوران دیگری وجود نداشته باشد 
        if not self.slug:
            
            self.slug = slugify(self.name, allow_unicode=True)
            
            unique_slug = self.slug
            num = 1
            while Restaurant.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1
                
            self.slug = unique_slug
        
        super().save(*args, **kwargs)

    

    def is_main_branch(self):
        return self.restaurant_parent is None # true false
        # if self.restaurant_parent:
        #     return False
        # return True
        
        
    # راه حل اول
    # بدون استفاده از related_name
    # همه برنچ ها زمانیکه restaurant_obj برنج اصلی هست 
    # # restaurant_obj.get_all_branches()
    # def get_all_branches(self):
    #     if self.is_main_branch():
    #         return Restaurant.objects.filter(restaurant_parent=self)
        
    # # والد رستوران کدام رستوران دیگر هست
    # # restaurant_obj.restaurant_parent
    
    # def show_related_branches(self):
    #     # اگر برنچ اصلی بود که برو تابع بالا رو صدا کن و زیر مجموعه هاش رو بگو
    #     if self.is_main_branch():
    #         return self.get_all_branches()
    #     # اگر برنج معمولی بود برو خواهر برادراش رو لیست کن نمایش بده
    #     if self.restaurant_parent:
    #         return Restaurant.objects.filter(restaurant_parent=self.restaurant_parent)

        
    # راه حل دوم 
    # با استفاده از related_name
    def get_all_branches(self):
        if self.is_main_branch():
            return self.branches.all()
        

    def show_related_branches(self):
        if self.is_main_branch():
            return self.get_all_branches()
        # شعبه اصلی نیست
        return self.restaurant_parent.branches.all() if self.restaurant_parent else None

    
    def update_average_rating(self):
        if self.rating_count > 0:
            self.average_rating = round(self.sum_rating / self.rating_count, 1)

    
    
    def __str__(self):
        return f"{self.name} -- {str(self.id)} "



# from django.contrib.auth.models import User
# Rating.objects.filter(name = 'zahra')
# rating_obj = Rating.objects.filter(user__username__contains = 'admin')
# %like%
# Rating.objects.filter(user__id = '1')
# Rating.objects.filter(user__firstname = 'zahra')
# rating_obj.restaurant.name
# اسم رستورانی که یوزر ادمین برایش امتیاز قرار داده


# resta_obj = Restaurant.objects.get(id=3)
# resta_obj.اسمی که به حدول rating.user.username
# resta_obj.rating_set
class Rating(models.Model):
    class Meta:
        unique_together = ('user', 'restaurant')
        verbose_name = "امتیاز"
        verbose_name_plural = "امتیازات"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='rating_set')
    rating = models.IntegerField(default=1, 
                                 validators=[
                                            MinValueValidator(1), 
                                            MaxValueValidator(5)
                                        ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} :: {self.restaurant.name} :: {self.rating}"
    
        
    def save(self, *args, **kwargs):
        """
        self.restaurant.rating_count += 1
        self.restaurant.sum_rating += self.rating
        self.restaurant.update_average_rating()
        super().save(*args, **kwargs)
        """
        if self.pk:
            # If the rating exists, we are updating an existing rating
            old_rating = Rating.objects.get(pk=self.pk)
            self.restaurant.sum_rating -= old_rating.rating
        else:
            # If the rating is new
            self.restaurant.rating_count += 1
            
        self.restaurant.sum_rating += self.rating
        self.restaurant.update_average_rating()
        self.restaurant.save()
        super().save(*args, **kwargs)
        
    
        
        
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
        
        
@receiver(post_delete, sender=Rating)
def update_restaurant_rating_on_delete(sender, instance, **kwargs):
    restaurant = instance.restaurant
    restaurant.rating_count -= 1
    restaurant.total_rating -= instance.rating
    # restaurant.update_average_rating()
    restaurant.save()
        
        
        

class Food(models.Model):
    class Meta:
        verbose_name = "غذا"
        verbose_name_plural = "غذا ها"
        
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="foods/", default='food-default.jpg')
    description = models.TextField()
    
    def __str__(self):
        return self.name
    


class Menu(models.Model):
    class Meta:
        verbose_name = "منو"
        verbose_name_plural = "منو ز"
        
    def restaurant_image_upload_to(instance, filename):
        path = f'restaurants_imgs/{instance.restaurant.id}_{instance.restaurant.name}/{instance.meal}/'
        return f'{path}/{filename}'
    
    
    MEAL_CHOICES = [
        ("breakfast", "صبحانه"),
        ("common", "وعده غذایی اصلی"),
        ("beverages", "نوشیدنی"),
        ("desserts", "سالاد "),
        ("others", "منو")
        # ("lunch", "ناهار")
        # ("dinner", "شام")
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="foods/", default='food-default.jpg')
    meal = models.CharField(max_length=50, choices=MEAL_CHOICES, default='others')
    food = models.ForeignKey("Food", on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    discount_percent = models.IntegerField(default=0, validators=[
                                            MinValueValidator(0), 
                                            MaxValueValidator(100)
                                        ])  # TODO: ولیدیشن ماکسیمم صد بودن تخفیف
    size = models.CharField(max_length=50)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE, null=True)
    description = models.TextField()

    def __str__(self):
        return f" {self.get_meal_display()}  -- {self.name} :: {self.food}  --  {self.restaurant.name}"
    
    def calc_price_after_discount(self):
        # return self.price - (self.discount * self.price)
        return self.price * (100 - self.discount_percent)   # 500 * 90%


    def get_food_name(self):
        return self.name if self.name else self.food.name

    def get_food_image(self):
        return self.image if self.image else self.food.image

    def get_food_desc(self):
        return self.description if self.description else self.food.description

