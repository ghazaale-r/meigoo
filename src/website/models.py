from django.db import models

# Create your models here.
class Contact(models.Model):
    class Meta:
        verbose_name = "کانتکت"
        verbose_name_plural = " کانتکت ها"
        
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    message = models.TextField()
    
    def __str__(self):
        return f"{self.email} --- message : {self.message[:50]}"
    
    
    