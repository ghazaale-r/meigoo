from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.
def contact_page(request):
    banner_message = {
        'h4' : 'ارتباط با ما',
        'msg' : '',
        'h2' : 'نظرات خود را نزد خود نگهدارید',
        
    }
    context = {
        'banner_message' : banner_message
    }
    return render(request, 'website\contact_page.html', context=context)



















from .forms import NameForm, ContactForm, ContactModelForm

def test_form_view(request):
    # request . method == GET
    form = ContactModelForm()
    
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        # form = ContactModelForm(data=request.POST)
        # print(form)
        if form.is_valid():
            form.save()
            # create contact object 
            #  save contact object 
            # return HttpResponse('ok')
        else:
            print(form.errors)
            # return HttpResponse('not valid')
            
            
    context = {
        'form' : form
    }
        
    return render(request, 'test_form/index.html', context)
        


# def test_form_view(request):
#     # post method and get post params
#     if request.method == 'POST':
#         print(request.POST)
#         form = ContactForm(request.POST)
        
#         if form.is_valid():
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             phone = form.cleaned_data["phone"]
#             message = form.cleaned_data["msg"]

#             contact_obj = Contact.objects.create(name=name, email=email, phone=phone, message=message)
            
#             # return HttpResponse("thanks")
#         else:
#             print(form.errors)
#             # print(form.cleaned_data)
#             # return HttpResponse("not valid") 
#     else:
#         form =  ContactForm()
        
        
        
        
#         # name = request.POST.get('name')
#         # email = request.POST.get('email')
#         # message = request.POST.get('msg')
#         # mobile = request.POST.get('phone')
        
#         # contact_obj = Contact()
#         # contact_obj.name = name
#         # contact_obj.email = email
#         # contact_obj.phone = mobile
#         # contact_obj.message = message
#         # contact_obj.save()
        
#     context = {
#         'form' :form
#     }
        
#     return render(request, 'test_form/index.html', context)

























# def test_form_view(request):
#     # post method and get post params of contact model 
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         message = request.POST.get('msg')
        
#         print(name, email, phone, message)
#         c_obj = Contact()
        
#         c_obj.name = name
#         c_obj.email = email
#         c_obj.phone = phone
#         c_obj.message = message
        
#         c_obj.save()
        
#     return render(request, 'test_form/index.html')





















# def test_form_view(request):
#     if request.method == "POST":
#         pass
#     form = ''
#     context = {
#         'form' : form
#     }
#     return render(request, 'test_form/index.html', context)





