from django.db import models
from django.db.models import PROTECT

from src.restaurant.special_models import Restaurant


# Create your models here.
# sql "create table restaurant (name text, ...")

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.PROTECT)
    order_count = models.IntegerField(default=0)
    count_view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    open_close = models.BooleanField(null=True, blank=True)
    restaurant_parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.DO_NOTHING)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.DO_NOTHING)
    # rating = models.FloatField(default=0)

    # main_branch = models.BooleanField(default=False, null=False)

    # open_close = models.NullBooleanField()
    def is_main_branch(self):
        if self.restaurant_parent:
            return False
        return True

    class Meta:
        ordering = ["updated_at"]
        verbose_name = "رستوران"
        verbose_name_plural = "رستوران ها"

    def __str__(self):
        return f"{self.name} -- {str(self.id)} "


class Food(models.Model):
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to="")
    description = models.TextField()


class Menu(models.Model):
    MEAL_CHOICES = [
        ("breakfast", "صبحانه"),
        ("common", "وعده غذایی اصلی"),
        ("beverages", "نوشابه"),
        ("desserts", "سالاد ")
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
    image = models.ImageField("")



    def calc_price_after_discount(self):
        # return self.price - (self.discount * self.price)
        return self.price * (100 - self.discount)   # 500 * 90%


class MenuTitle(models.Model):
    pass
