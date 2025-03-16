# Update this in main_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/add/', views.add_product, name='add_product'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('api/stats/', views.user_activity_stats, name='user_activity_stats'),
]
