# main_app/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Product, UserActivity
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'main_app/home.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    
    return render(request, 'main_app/add_product.html', {'form': form})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Log user activity in MongoDB - router will handle the database selection
    UserActivity(
        user_id=request.user.id if request.user.is_authenticated else 0,
        action='view_product',
        page=f'product/{pk}',
        metadata={'product_id': pk}
    ).save()  # No 'using' parameter needed
    
    return render(request, 'main_app/product_detail.html', {'product': product})

def user_activity_stats(request):
    # The router will handle database selection automatically
    page_views = UserActivity.objects.filter(
        action='view_product'
    ).count()
    
    return JsonResponse({'page_views': page_views})

def dashboard(request):
    """
    View function for the analytics dashboard page.
    Displays statistics about products and provides data for MongoDB analytics.
    """
    products = Product.objects.all()
    in_stock = products.filter(stock__gt=0).count()
    out_of_stock = products.filter(stock=0).count()
    
    context = {
        'products': products,
        'in_stock': in_stock,
        'out_of_stock': out_of_stock
    }
    
    return render(request, 'main_app/dashboard.html', context)
