from django.db import models
from category.models import category
# Create your models here.



class Product(models.Model):
    product_name = models.CharField(max_length=250, unique=True)
    product_brand = models.CharField(max_length=100, default='')
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_specs = models.TextField()
    product_image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField()
    category = models.ForeignKey(category, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.product_name




































