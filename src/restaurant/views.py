from django.shortcuts import render, get_object_or_404

from .models import Category, Restaurant


# # Create your views here.
# def test_home_page(request):
#     # orm 
#     categories = Category.objects.all()
#     """select * form restaurant_Category"""
#     context = {
#         'food_part_available' : True,
#         'categoriiis' : categories
        
#     }
#     # return render(request, 'index.html')
#     return render(request, 'restaurant/home_page.html', context)


def restaurant_page_with_category(request, category_id=None):
    
    
    categories = Category.objects.all()
    
    if not category_id:
        restaurants = Restaurant.objects.all()
    else:
        categories_obj = Category.objects.get(id=category_id)
        # categories_obj = get_object_or_404(Category, pk=category_id)
        
        selected_category = categories_obj
        restaurants = Restaurant.objects.filter(categories=categories_obj)
        
    context = {
        'categories' : categories,
        # 'restaurants' : restaurants,
        'selected_category' : selected_category
    }
    
    return render(request, 'restaurant/restaurants.html', context)
