from contextlib import ContextDecorator
from distutils.command.upload import upload
from operator import mod
from typing import Optional
from django.db import models
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import  BaseUserManager,AbstractBaseUser,PermissionsMixin




# Create your models here.

class manager(BaseUserManager):

    def normalize_email(self,name):
        return name.strip().lower()
    use_in_migrations=True

    def __create(self,username,email,password):
        if not email and not password and not username:
            raise ValueError("you should have a email")
        user=self.model(email=self.normalize_email(email),username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create(self,**kwargs):
        user=self.__create(kwargs.get("username"),kwargs.get("email"),kwargs.get("password"))
        user.save()
        return user
   
    def create_superuser(self,username,email,password):
        user= self.__create(username,email,password)
        user.is_admin= True
        user.save()
        return user
    
   


class Users(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=20)
    created_date=models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects=manager()
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['username']
    def __str__(self):
        return self.email

    def has_module_perms(self , app_label):
        return self.is_admin

    def has_perm(self, perm: str, obj=None ) -> bool:
        if self.is_admin:
            return True
        return super().has_perm(perm, obj)
    
    @property
    def is_staff(self,):
        return self.is_admin
    class Meta:
        db_table ="User"
        verbose_name = "User"


class Profile(models.Model):
    user=models.OneToOneField(Users,on_delete=models.CASCADE,null=True)
    fullname=models.CharField(max_length=20)
    contact=models.CharField(max_length=10)
    country=models.CharField(max_length=40)
    profession=models.CharField(max_length=50)
    image=models.ImageField(upload_to='images',blank=True,null=True)
   
    def __str__(self):
        return str(self.user)
    class Meta:
        db_table="Profile"
