from django.db import models
from store.models import Product
# Create your models here.



class Cart(models.Model):
    cart_id = models.CharField(max_length=500, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def sub_total(self):
        return self.product.product_price * self.quantity

    def __str__(self):
        return f'{self.product}'





















