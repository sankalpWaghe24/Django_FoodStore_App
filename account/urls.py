from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [
   path("register-admin",register_admin,name="RegisterAdmin"),
   path("register-customer",register_customer,name="RegisterCustomer"),
   path("login",mylogin,name="Login"),
   path("logout",mylogout,name="Logout"),
]