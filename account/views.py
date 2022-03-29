from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import MyUser
# Create your Account views here.


def register_admin(request):
    if request.method == "POST":
        form = AdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success( request, "Dear Admin Your account has been registered successfully")
            return redirect('Login')
        else:
            messages.error(request, "Registration Unsuccessfull")
    else:
        form = AdminForm()
    context =  {"form": form}
    return render(request, "account/register.html",context)


def register_customer(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Dear Customer Your Account has been Successfully registered")
            return redirect('Login')
        else:
            messages.error(
                request, "Registration Unsuccessfull.. Something went wrong")
    else:
        form = UserForm()
    context =  {"form": form}
    return render(request, "account/register.html",context)


def mylogin(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        contact = request.POST['username']
        password = request.POST['password']
        if contact and password and contact.isdigit():
            user = authenticate(request,username=contact, password=password)
            if user:
                login(request, user)
                messages.success(request, "Login Successfully")
                return redirect('Home')
        else:
            messages.error(request, " Please Enter Valid UserName | Password")

    else:
        form = AuthenticationForm()
    context =  {"form": form}
    return render(request, "account/register.html",context)


def mylogout(request):
    logout(request)
    messages.success(request, "Logout Successfull")
    return redirect("Login")

