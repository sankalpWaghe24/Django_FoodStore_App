from django.contrib.auth.models import AbstractBaseUser
from django.db import models
'''
   Customization of User Model of AUth APp can be done
      1. AbstractUser
            adds some extra field in user models
            
      2. AbstractBaseUser
            creating customs field from scratch without using django's built-in fields
            it also need to be create its own UserManager in AbstractBaseUser.
            
            BaseUserManager contains 2 methods :
               1. Create User 
               2. Create SuperUser
               
               setpassword : used to encrpt the password
               object : is  the name of the default Manager
               username_field : which helps for login
'''
# ? Create your Account models here.


# ? Creating User Manager
from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, contact, password, **extra_fields):
        if not contact:
            raise ValueError("User must have an Mobile Number")
        user = self.model(contact=contact,  **extra_fields)
        user.set_password(password)
        user.save(self._db)
        return user;

    def create_superuser(self, contact, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_Role', 'owner')
        return self.create_user(contact, password, **extra_fields)


# ? Creating Custom Auth using AbstractBaseUser


class MyUser(AbstractBaseUser):
    userId = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.BigIntegerField(unique=True)
    user_Role = models.CharField(max_length=10)
    is_superuser = models.BooleanField(default=False)
    address = models.TextField()

    objects = MyUserManager()  # ? Manager created
    USERNAME_FIELD = "contact"
    REQUIRED_FIELDS = ("first_name", "last_name")
