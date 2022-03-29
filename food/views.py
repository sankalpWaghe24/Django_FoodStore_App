from django.views.generic.edit import UpdateView, DeleteView,CreateView

from django.shortcuts import render

# Create your views here.
# ? django built-in
from django.contrib.messages.views import SuccessMessageMixin

# ? custom
from .models import Food
from .forms import FoodForm
from django.urls import reverse_lazy


#  ? Food Menu/List
from django.views.generic.list import ListView


class FoodListView(ListView):
    model = Food
    template_name = "food/foodlist.html"


class FoodCreateView(SuccessMessageMixin, CreateView):
    model = Food
    form_class = FoodForm
    template_name = "food/foodform.html"
    success_url = reverse_lazy("foodlist")
    success_message = 'Food is Added Successfully'


class FoodUpdateView(SuccessMessageMixin, UpdateView):
    model = Food
    form_class = FoodForm
    template_name = "food/foodform.html"
    success_message = 'Food is Updated Successfully...'
    success_url = reverse_lazy("foodlist")


class FoodDeleteView(SuccessMessageMixin, DeleteView):
    model = Food
    template_name = "food/deleteConfirm.html"  # ? works as Confirmation message
    success_message = 'Food is Deleted Successfully'
    success_url = reverse_lazy("foodlist")
