from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):

    def create_user(self,email,first_name, last_name ,address,dob,company,password=None):
        # if username is None:
        #     raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a Email')
        username = first_name + last_name
        print(username)
        user = self.model(first_name=first_name,last_name=last_name, email=self.normalize_email(email),address=address,dob = dob,company = company)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Password should not be none')
        user = self.model( email=self.normalize_email(email))
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user


# AUTH_PROVIDERS = {'email': 'email'}


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255,blank = True,null = True)
    last_name = models.CharField(max_length=255 ,blank = True ,null = True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # auth_provider = models.CharField(
    #     max_length=255, blank=False,
    #     null=False, default=AUTH_PROVIDERS.get('email'))
    address = models.TextField(null = True)
    dob = models.DateField(blank=True,null=True)
    company = models.CharField(max_length=500,null = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }