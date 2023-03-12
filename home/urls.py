from django.urls import path
from . import views
from .views import ProductDetailView


app_name = 'home'




urlpatterns = [
    path('', views.home, name = 'home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name = 'product_detail')
]



























