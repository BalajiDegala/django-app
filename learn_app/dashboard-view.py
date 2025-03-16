# Add this to main_app/views.py

def dashboard(request):
    products = Product.objects.all()
    in_stock = products.filter(stock__gt=0).count()
    out_of_stock = products.filter(stock=0).count()
    
    context = {
        'products': products,
        'in_stock': in_stock,
        'out_of_stock': out_of_stock
    }
    
    return render(request, 'main_app/dashboard.html', context)
