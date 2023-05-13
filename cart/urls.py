from django.urls import path
from .views import cart, add_cart, delete_cart, remove_cart, checkout

app_name = 'cart'

urlpatterns = [
    path('', cart, name='cart'),
    path('add_cart/<int:pk>', add_cart, name='add_cart'),
    path('delete_cart/<int:product_id>', delete_cart, name="delete_cart"),
    path('remove-cart/<int:product_id>', remove_cart, name='remove_cart'),
    path('checkout/', checkout, name='checkout')
]


















