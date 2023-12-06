from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, AnonymousUser
# Create your models here.

class MyAccountManager(BaseUserManager):
    """creating the user"""
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('You must have valid email')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    """creating super user"""
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = self.normalize_email(email),
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.is_authenticated = True
        user.is_anonymous = False
        user.save(using=self._db)
        return user




class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, unique=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=200)
    
    """some other required fields"""
    
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_authenticated = True
    is_anonymous = False
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','username']
    objects = MyAccountManager()
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_lable):
        return True


















































































































