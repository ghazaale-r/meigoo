
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.sessions.models import Session
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import RestaurantManager, Customer
from .forms import CustomerSignUpForm, CustomUserSignUpForm


def test(request):
    context = {}
    # session_key = request.session.get('sessionid') # Wrong
    session_key = request.COOKIES.get('sessionid', None)
    
    print('session_key : ' , session_key)
    if session_key :

        # واکشی سشن از پایگاه داده
        session = Session.objects.get(session_key=session_key)

        # دیکد داده‌های سشن
        print(session.session_data)
        session_data = session.get_decoded()
        print(session_data)
    
    
    # set data to a session
    request.session['user_name'] = 'example_user'

    # get / fetch data from session
    user_name = request.session.get('user_name', 'Guest')
    context['user_name'] = user_name
    print(user_name)

    # get / fetch data from COOKIES
    user_id = request.COOKIES.get('user_id', 'Not Set')
    print(user_id)
    context['user_id'] = user_id
    
    # set data to COOKIES
    response = render(request, 'accounts/test.html', context)
    
    response.set_cookie('user_id', '123456')
    return response

# ==================================================
# def login_view(request):
#     return render(request, 'accounts/login.html')
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view222(request):
    # None.is_authenticated error
    if request.user.is_authenticated:
        # redirect home page --- user profile
        return redirect('/')
        
    # print(request.user.is_authenticated)
    # print(request.user.username)
    # print(request.user.first_name)
    # print(request.user.email)
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["pass"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
            # ...
        else:
            return HttpResponse('Invalid login')
        # Return an 'invalid login' error message.
        
    return render(request, 'accounts/login.html')


# def login_view(request):
#     print(request.user)
#     # این ۴ خط بعدی را یا میتوان درون متد ویو انجام داد 
#     # یا درون فایل تمپلیت

#     # درون متد ویو
#     if request.user.is_authenticated:
#         msg = f"{request.user.username} is logged in "
#     else:
#         msg = "user is not authenticated"
        
#     context = {
#         'msg' : msg
#     }
#     return render(request, 'accounts/login.html')



# def login_view2(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
            
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('/')
#                 # Redirect to a success page.
#         else:
#             print(form.errors)
#             # Return an 'invalid login' error message.
#             return HttpResponse(' invalid login')
            
#     context = {
#         'form' : AuthenticationForm()
#     }
#     return render(request, 'accounts/login.html', context)



def login_view(request):
    if request.user.is_authenticated:
        # redirect home page --- user profile
        return redirect('/')
    
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                 # Redirect to a success page.
                if request.GET.get('next'):
                    return redirect(request.GET['next'])
                
                if RestaurantManager.objects.filter(pk=user.pk).exists():
                    return redirect(reverse('accounts:manager_profile', kwargs={'pk': user.pk}))
                
                return redirect('/')
                # return HttpResponse("User has logged in!")
            else:
                return HttpResponse('Invalid login')
            
    context = {'form':form}
    return render(request, 'accounts/login.html', context=context)

# ==================================================
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

@login_required()
def logout_view(request):
    # if request.user.is_authenticated():
    logout(request)
    return redirect('/')
    
        # return 


# ==================================================
from django.contrib.auth.models import User

def signup_view(request):  
    form = CustomUserSignUpForm()
    
    if request.method == 'POST':
        form = CustomUserSignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
            # redirect to login page
            # return redirect('accounts/login')
            return redirect(reverse('accounts:login'))
        # else:
        #     return HttpResponse('invalid sign up')
            
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # user_obj = User()
            # user_obj.username = username
            # user_obj.password = password
            # user_obj.save()
            

        
    
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

