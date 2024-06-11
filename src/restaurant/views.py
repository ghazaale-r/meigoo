from django.shortcuts import render

from .models import Category


# Create your views here.
def test_home_page(request):
    
    categories = Category.objects.all()
    context = {
        'food_part_available' : True,
        'categoriiis' : categories
        
    }
    # return render(request, 'index.html')
    return render(request, 'restaurant/home_page.html', context)


