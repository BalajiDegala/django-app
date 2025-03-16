# main_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, UserActivity
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'main_app/home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Log user activity in MongoDB
    UserActivity(
        user_id=request.user.id if request.user.is_authenticated else 0,
        action='view_product',
        page=f'product/{pk}',
        metadata={'product_id': pk}
    ).save(using='mongodb')
    
    return render(request, 'main_app/product_detail.html', {'product': product})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    
    return render(request, 'main_app/add_product.html', {'form': form})

def user_activity_stats(request):
    # Example of querying MongoDB
    page_views = UserActivity.objects.using('mongodb').filter(
        action='view_product'
    ).count()
    
    return JsonResponse({'page_views': page_views})
