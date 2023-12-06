from django.shortcuts import render
from store.models import Product
from django.views.generic import DetailView
# Create your views here.




def home(request):
    page_obj = products = Product.objects.values('pk','product_image','product_name','product_price').filter(is_available=True).order_by('-created_date')
    product_name = request.GET.get('Product_product_name')
    if product_name != '' and product_name is not None:
        page_obj = products.filter(product_name__icontains=product_name)
    context = {
        'products': products,
        'page_obj': page_obj
    }
    return render(request, 'home/home.html', context)



class ProductDetailView(DetailView):
    model = Product






















































