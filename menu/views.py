from django.shortcuts import render
from .models import Category

def menu_list(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'menu/index.html', {'categories': categories})