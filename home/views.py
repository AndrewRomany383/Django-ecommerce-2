from django.shortcuts import render
from store.models import Product
from django.views.generic import DetailView
# Create your views here.




def home(request):
    products = Product.objects.values('pk','product_image','product_name','product_price').filter(is_available=True).order_by('-created_date')
    context = {
        'products': products
    }
    return render(request, 'home/home.html', context)



class ProductDetailView(DetailView):
    model = Product






















































