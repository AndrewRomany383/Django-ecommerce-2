from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import category
# Create your views here.



def store(request, slug=None):
    categories = None
    products = None
    if slug != None:
        categories = get_object_or_404(category, slug=slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.values('pk','product_image','product_name','product_price').order_by('-created_date')
        product_count = products.count()
    context = {
        'products':products,
        'product_count':product_count
    }
    return render(request, 'store/store.html', context)




















































































































