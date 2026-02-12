from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('qr/', views.qr_code_view, name='qr_code'),
]