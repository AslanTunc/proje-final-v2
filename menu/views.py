from django.shortcuts import render
from .models import Category, MenuItem

def menu_list(request):
    categories = Category.objects.prefetch_related('items').all()
    
    context = {
        'categories': categories,
    }
    return render(request, 'menu/index.html', context)