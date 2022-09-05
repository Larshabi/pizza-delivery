from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("Email should be provided"))
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_admin', True)
        if other_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser should have is_staff as True"))
        if other_fields.get('is_superuser') is not True:
                raise ValueError(_("Superuser should have is_superuser as True"))
        if other_fields.get('is_active') is not True:
                raise ValueError(_("Superuser should have is_active as True"))
        if other_fields.get('is_admin') is not True:
                raise ValueError(_("Superuser should have is_admin as True"))
        
        user = self.create_user(email, password, **other_fields)
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    
    username= models.CharField(max_length=25, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    phone = PhoneNumberField(null=False)
    is_admin = models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS= ["username"]
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    