from django.contrib import admin
from .views import *
from django.urls import path
from django.views.generic.base import TemplateView
urlpatterns = [
   path("",TemplateView.as_view(template_name="index.html") , name="Home"),
   path("createFood" ,FoodCreateView.as_view(), name="addfood" )   ,
   path("foodlist",FoodListView.as_view(), name="foodlist"),
   path("updatefood/<int:pk>",FoodUpdateView.as_view(), name="updatefood"),
   path("delete/<int:pk>",FoodDeleteView.as_view(), name="delete"),
]
