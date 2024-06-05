from django.db import models

# Create your models here.
# sql "create table restaurant (name text, ...")

class Restaurant(models.Model):
    
    name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)
    order_count = models.IntegerField(default=0)
    count_view = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    open_close = models.BooleanField(null=True, blank=True)
    # open_close = models.NullBooleanField()
    

    def __str__(self):
        return f"{self.name} -- {str(self.id)} "
    