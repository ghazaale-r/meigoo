from django.db import models

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import (AbstractUser, User,
    BaseUserManager, AbstractBaseUser, PermissionsMixin)

from django.contrib.auth.base_user import BaseUserManager

from django.utils import timezone
from django.core.validators import ( MinLengthValidator, MaxLengthValidator,
                                        MinValueValidator, MaxValueValidator)
# Create your models here.
from django.conf import settings



class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("The Email must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model - use email instead of username
    """
    email = models.EmailField(max_length=255, unique=True)
    # برای دسترسی یوزر به پنل ادمین باید استف باشد
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_customer = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    # profile = 

    # با حذف فیلد username
    # باید بهش بگیم شاخصی که برای ورود هست کدام فیلد هست
    USERNAME_FIELD = "email"
    # یکسری موراد دیگه مثل نام و نام خانوادگی اگر بخواهیم اجباری باشند
    REQUIRED_FIELDS = []
    
    class Meta:
        
        verbose_name="کاربر"
        verbose_name_plural = 'کاربران' 

    # objects = CustomUserManager()
    objects = UserManager()

    def __str__(self):
        return self.email
    
    def get_profile_url():
        return 'profile/'
    
    def is_manager(self):
        return self.is_staff and not self.is_superuser and not self.is_customer
     
    def is_is_customer(self):
        return not self.is_staff and self.is_customer
     
    
# مدیر رستوران 
# ثبت نام انجام دهد 


## فرم ثبت نام 
# شماره تلفن یا ایمیل
# پسورد
# نام رستوران
# ادرس رستوران

# erd

# جدول رستوران
# اسم رستوران
# ادرس رستوران
# مدیر - ریلیشن - 

# جدول کاربرسایت مدیر رستوران
# شماره تلفن یا ایمیل 
# پسورد

# class RestaurantManager(User):
#     # filed email password
#     # نری یه جدول جدید بسازی
#     # من اصلا اینجا بهت فییلدی ندادم
    
#     class Meta:
#         proxy = True
        
#     def get_profile_url():
#         return 'managers/restaurants/'
    
#     def save(self):
#         self.is_superuser = False
#         self.is_staff = True
#         return super().save()
      
# user_obj  = User(email, password)
# user_obj.save()

# shila_m = RestaurantManager(email, password)      
# shila_m.save()
# admin_obj = Admin(email, password)      
# admin_obj.save()

# وجه تمایز دو ابجکت بالا
# برای یوزر معمولی هیچی همون دیفالت هایی که در مدل نوشتیم

# برای مدیر رستوران

# is_superuser = False
# is_staff = True


class Admin(User):
    # filed email password
    # نری یه جدول جدید بسازی
    # من اصلا اینجا بهت فییلدی ندادم
    
    class Meta:
        proxy = True
        verbose_name="ادمین"
        verbose_name_plural = 'ادمین ها' 
        
    def get_profile_url():
        return 'admin/dashboard/'
        # return reversed('dashboard')
    
    def save(self):
        self.is_superuser = True
        self.is_staff = True
        
        return super().save()
    
    
# views.py
# after login

# request.user

# redirect request.user.get_profile_url

# صفحه ثبت نام

# مدیر رستوان 
# مشتری

# ایجاد 
    
# from django.conf import settings
# user_class = settings.Auth user model 
# class profile(models.Model):
#     owner = models.ForeignKey(user_class, related_name=")
    
# super user

# is_superuser = T
# is_staff = T
    
    
    
# restaurant manager
# # is_restaurant_manager = T / F
# # no extra fields
# is_superuser = F
# is_staff = T

# email password , name rest, addr rest, ...

# class rest_maanger(models.Model):
#     email
#     password
    
    

# customer 
# is_customer  = T / F

# address - multi  - 1
# default - address 



# customer 
#       email , pass ,  address , main_addre 

#         m2m

# customeraddress
#     main_addres
#     foreign key customer
#     foreign key address


# address
#   city 
#   state
#   zipcode
  
# # is_superuser = F
# # is_staff = F  
    
    
    

# class RestaurantManagerManager(BaseUserManager):
#     def create_restaurant_manager(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', False)
#         extra_fields.setdefault('is_active', True)
#         # extra_fields.setdefault('is_restaurant_manager', True) 

#         if not email:
#             raise ValueError("The Email must be set")
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def get_queryset(self):
#         return super().get_queryset().filter(is_staff=True, is_superuser=False)



class RestaurantManagerManager(UserManager):
    def create_restaurant_manager(self, email, password, **extra_fields):
        # extra_fields.setdefault('is_restaurant_manager', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)

        return super().create_user(email, password, **extra_fields)
    
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True, is_superuser=False)


    

class RestaurantManager(User):
    objects = RestaurantManagerManager()

    class Meta:
        proxy = True
        verbose_name="مدیر رستوان"
        verbose_name_plural = 'مدیر رستوران ها' 

    def get_profile_url(self):
        return "/restaurant_manager/profile/"
    
    def save(self, *args, **kwargs):
        self.is_staff = True
        self.is_superuser = False
        self.is_active = True
        # self.is_restaurant_manager = True
        super().save(*args, **kwargs)


# RestaurantManager.objects.create_restaurant_manager()
# RestaurantManager.objects.all()
# # همه یوزر ها را بر میگرداند 
# من میخواهم فقط 
# مدیران رستوران ها را برگرداند
    

    
class CustomerManager(UserManager):
    def create_customer(self, email, password, **extra_fields):
        extra_fields.setdefault('is_customer', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return super().create_user(email, password, **extra_fields)
    


# Customer.objects.all()
    
    
    
# multi table
class Customer(User):
    objects = CustomerManager()
    address = models.ManyToManyField('Address', through='CustomerAddress', related_name='customeraddress')

    class Meta:
        verbose_name="مشتری"
        verbose_name_plural = 'مشتری ها' 
        
    def save(self,*args, **kwargs):
        if not self.id:
            self.is_staff = False
            self.is_superuser = False
            self.is_customer = True
        return super(Customer,self).save(*args,**kwargs)

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False

class CustomerAddress(models.Model):
    main_address = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True, related_name='customer2')
    address = models.ForeignKey('Address', on_delete=models.SET_NULL , null=True,related_name='address_related')

    class Meta:
        verbose_name = "آدرس مشتری"
        verbose_name_plural = "آدرس مشتریان"
        
    def __str__(self) -> str:
        return f"{self.customer}-address"




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
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='owner',on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return f"{self.state}, {self.city}, {self.street}"
    
    
    
class Profile(models.Model):
    class Meta:
        verbose_name = "پروفایل"
        verbose_name_plural = "پروفایل ها"
        
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    


# from django.db.models.signals import post_save
# from django.dispatch import receiver


from django.contrib.auth import get_user_model

Usermodel = get_user_model()

# @receiver(post_save, sender=Usermodel)
# def save_profile(sender, instance, **kwargs):
#     print("this is post save signal method")
#     instance.profile.save()




@receiver(post_save, sender=Usermodel)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=Customer)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
@receiver(post_save, sender=RestaurantManager)
def save_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        