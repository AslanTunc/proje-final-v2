from django.shortcuts import render
from .models import Category, MenuItem

def index(request):
    categories = Category.objects.prefetch_related('menuitem_set').all()
    
    context = {
        'categories': categories,
    }
    return render(request, 'menu/index.html', context)