from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

from .forms import NameForm, ContactForm, ContactModelForm
from .forms import CategoryModelForm

# class based views
from django.views.generic import TemplateView, RedirectView

from django.views.generic import (
                            ListView,
                            DetailView,
                            FormView,
                            CreateView,
                            UpdateView,
                            DeleteView
                                  )
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from restaurant.models import Category

from django.shortcuts import reverse
from django.urls import reverse_lazy
# from django.views.generic.edit import FormView









from django.http import HttpResponse
from django.views import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('get result')

    def post(self, request):
        # <view logic>
        return HttpResponse('post result')

    # def put(self, request):
    #     # <view logic>
    #     return HttpResponse('put result')

    # def patch(self, request):
    #     # <view logic>
    #     return HttpResponse('patch result')

    # def delete(self, request):
    #     # <view logic>
    #     return HttpResponse('delete result')















# @csrf_exempt
def index_f_view(request):
    return render(request, 'index.html')














class IndexTemplateView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["latest_articles"] = Article.objects.all()[:5]
        context["name"] = "ali"
        return context

    # while using TemplateView
    # just sent GET method and set context data if needed
    # dont pass forms
    # dont use another method like post put delete 















class DjangoRedirectView(RedirectView):
    url = ""
    permanent = False
    query_string = True
    pattern_name = "article-detail"

    def get_redirect_url(self, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs["pk"])
        article.update_counter()
        return super().get_redirect_url(*args, **kwargs)













class CategoryListView(ListView):
    # queryset  = Category.objects.filter(active=True)
    # queryset  = Category.objects.filter(manager=request.user)
    # queryset  = Category.objects.all()
    model = Category
    context_object_name = "categories"
    
    # def get_queryset(self):
    #     cats = Category.objects.all()
    #     # cats = Category.objects.filter()
    #     return cats
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["hi"] = 'Doroud'
        
        # context['rest'] = Restaurant.objects.all()
        return context
    
    
    
    
    
    
    
    
    
    
    
    
    
# manager 

# create address  createview
# create restaurant  createview # user logged in set as manager


# restarant all -- list view
# just see restaurant detail --- DetailView
# edit restaurant --- UpdateView
# del rest --- deleteview 



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







class CategoryDetailView(DetailView):
    model = Category
    pk_url_kwarg = 'id'
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context










class CategoryFormView(FormView):
    template_name = "cat.html"
    form_class = CategoryModelForm
    success_url = reverse_lazy('website:category-list')
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

    
    
class ContactFormView(FormView):
    # template_name = "contact.html"
    form_class = ContactModelForm
    # success_url = reverse('website:category-list')
    success_url = reverse_lazy('website:category-list')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)












class CategoryCreateView(CreateView):
    model = Category
    # fields = '__all__'
    form_class = CategoryModelForm
    success_url = reverse_lazy('website:category-list')
    















class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryModelForm
    # success_url = '/category/'
    # wrong error
    # success_url = reverse('website:category-list')
    
    success_url = reverse_lazy('website:category-list')













class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('website:category-list')






# Create your views here.
def contact_page(request):
    
    form = ContactModelForm()
    
    if request.method == 'POST':
        # data = {
        #     'name' : 'ali'
        #     'email' : 'sdlfj@lkd.com'
        # }
        # data.update(request.POST)
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    
    banner_message = {
        'h4' : 'ارتباط با ما',
        'msg' : '',
        'h2' : 'نظرات خود را نزد خود نگهدارید',
        
    }
    context = {
        'banner_message' : banner_message,
        'form' : form
    }
    return render(request, 'website\contact_page.html', context=context)
























# def test_form_view(request):
#     # request . method == GET
#     form = ContactModelForm()
    
#     if request.method == 'POST':
#         form = ContactModelForm(request.POST)
#         # form = ContactModelForm(data=request.POST)
#         # print(form)
#         if form.is_valid():
#             form.save()
#             # create contact object 
#             #  save contact object 
#             # return HttpResponse('ok')
#         else:
#             print(form.errors)
#             # return HttpResponse('not valid')
            
            
#     context = {
#         'form' : form
#     }
        
#     return render(request, 'test_form/index.html', context)
        


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





