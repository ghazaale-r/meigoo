from django import forms
from .models import Contact

class NameForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    

class ContactForm(forms.Form):
    name = forms.CharField(label="نام" , max_length=100)
    email = forms.EmailField(label="ایمیل", max_length=100)
    phone = forms.CharField(label="تلفن" ,max_length=11, help_text="شماره تلفن شما باید کمتراز ۱۱ کارکتر باشد")
    msg = forms.CharField(label="پیام", widget=forms.Textarea)
    
    
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        labels = {
            'name' : 'نام',
            'email' : 'ایمیل',
        }
        help_texts = {
            "phone": 'باید کمتر از ۱۱ رقم باشد',
        }