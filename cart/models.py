from account.models import MyUser
from django.db import models
from food.models import Food

# Create your models here.
from django import template
register = template.Library()


class CartItem(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def get_total(self):
        total = self.food.foodPrice * self.quantity
        return total

    def __str__(self):
        return f"{self.quantity} "


class Cart(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    itemlist = models.ManyToManyField(CartItem)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user.first_name} - {self.itemlist.all()} items. "

    def __repr__(self) -> str:
        return f"{self.user.first_name} - {len(self.itemlist.all())} items. "

    @property
    def get_cart_total(self):
        orderitems = self.itemlist.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.itemlist.all()
        total = sum([item.quantity for item in orderitems])
        return total
