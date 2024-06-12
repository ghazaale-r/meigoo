from datetime import datetime


from django.db import models
from django.contrib.auth.models import User
from django.core.validators import ( MinLengthValidator, MaxLengthValidator,
                                        MinValueValidator, MaxValueValidator)
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
        
        



# Create your models here.
# sql "create table restaurant (name text, ...")

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10, blank=True,
                               validators=[
                                   MinLengthValidator(10),
                                    MaxLengthValidator(10)
                               ])

    def __str__(self):
        return f"{self.state}, {self.city}, {self.street}"
    
    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس ها"
        
        
class Category(models.Model):
    def restaurant_image_upload_to(instance, filename):
        # filename = 'skdfhkj.jpg'
        filename = f'{instance.id}-{filename}' if instance.id else filename
        return f'cats_im/{datetime.now().strftime("%Y-%m/")}/{filename}'
    
    name = models.CharField(max_length=100)
    image_11 = models.ImageField(upload_to='categories_images/', blank=True, null=True)
    image_22 = models.ImageField(upload_to ='cats_img/%Y/%m/%d/', default='default.jpg') 
    image_33 = models.ImageField(upload_to =restaurant_image_upload_to, blank=True, null=True)
    # restaurants = این رو برو وصل کن به رستوران ها
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"



class Restaurant(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    
    image = models.ImageField(upload_to ='restaurants_imgs/%Y/%m/', default='default.jpg') 
     
    order_count = models.IntegerField(default=0)
    count_view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.DateTimeField(null=True, blank=True)
    
    open_close = models.BooleanField(null=True, blank=True)
    # open_close = models.NullBooleanField()
    
    restaurant_parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.DO_NOTHING)
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

    class Meta:
        ordering = ["updated_at"]
        verbose_name = "رستوران"
        verbose_name_plural = "رستوران ها"


    def is_main_branch(self):
        return self.restaurant_parent is None
        # if self.restaurant_parent:
        #     return False
        # return True
        
        
    # راه حل اول
    # بدون استفاده از related_name
    def get_all_branches(self):
        if self.is_main_branch():
            return Restaurant.objects.filter(restaurant_parent=self)
        

    def show_related_branches(self):
        if self.is_main_branch():
            return self.get_all_branches()
        if self.restaurant_parent:
            return Restaurant.objects.filter(restaurant_parent=self.restaurant_parent)

        
    # راه حل دوم 
    # با استفاده از related_name
    def get_all_branches(self):
        if self.is_main_branch():
            return self.branches.all()
        

    def show_related_branches(self):
        if self.is_main_branch():
            return self.get_all_branches()
        return self.restaurant_parent.branches.all() if self.restaurant_parent else None

    
    def update_average_rating(self):
        if self.rating_count > 0:
            self.average_rating = round(self.sum_rating / self.rating_count, 1)
        else:
            self.average_rating = 0.0
        self.save()

    
    
    def __str__(self):
        return f"{self.name} -- {str(self.id)} "



# from django.contrib.auth.models import User
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, 
                                 validators=[
                                            MinValueValidator(1), 
                                            MaxValueValidator(5)
                                        ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'restaurant')
        
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
        super().save(*args, **kwargs)
        
        
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
        
        
@receiver(post_delete, sender=Rating)
def update_restaurant_rating_on_delete(sender, instance, **kwargs):
    restaurant = instance.restaurant
    restaurant.rating_count -= 1
    restaurant.total_rating -= instance.rating
    restaurant.save()
        
        
        
        
        
        
        
        
        

class Food(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="")
    description = models.TextField()


class Menu(models.Model):
    MEAL_CHOICES = [
        ("breakfast", "صبحانه"),
        ("common", "وعده غذایی اصلی"),
        ("beverages", "نوشیدنی"),
        ("desserts", "سالاد "),
        ("others", "منو")
        # ("lunch", "ناهار")
        # ("dinner", "شام")
    ]
    meal = models.CharField(max_length=50, choices=MEAL_CHOICES)
    food = models.ForeignKey("Food", on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=3)
    discount = models.IntegerField(default=0)  # TODO: ولیدیشن ماکسیمم صد بودن تخفیف
    size = models.CharField(max_length=50)
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE, null=True)
    description = models.TextField()
    # image = models.ImageField("")



    def calc_price_after_discount(self):
        # return self.price - (self.discount * self.price)
        return self.price * (100 - self.discount)   # 500 * 90%


class MenuTitle(models.Model):
    pass