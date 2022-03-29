import django_filters

from cart.models import Cart


from .models import *
class OrderFilter(django_filters.FilterSet):
   class Meta:
      model = Cart
      fields = '__all__'
   
   