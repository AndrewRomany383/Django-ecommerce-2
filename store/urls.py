from django.urls import path
from .views import store
from cart.views import add_cart


urlpatterns = [
    path('', store, name='store'),
    path('<slug:slug>/', store, name='product_by_category'),
    path('add_cart/<int:product_id>', add_cart, name='add_cart'),
]















































