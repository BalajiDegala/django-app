# main_app/admin.py

from django.contrib import admin
from .models import Product, UserActivity


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')

@admin.register(UserActivity)
class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'action', 'page', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('user_id', 'page')

    def get_queryset(self, request):
        # Use the MongoDB database
        return super().get_queryset(request).using('mongodb')
    

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

