from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

class UserManage(BaseUserManager):

    def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("O usuário precisa ter um endereço de email")
        if not password:
            raise ValueError("O usuário precisa ter uma senha")
        if not full_name:
            raise ("O usuário precisa ter o nome completo")

        user_obj = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.full_name = full_name
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,full_name, email, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
        )

        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(
            email,
            full_name,
            password=password,
            is_staff=True,
            is_admin=True,

        )
        return user

class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True) # Can login
    staff = models.BooleanField(default=False) # Member of Staff
    admin = models.BooleanField(default=False) # SuperUSer
    timestamp = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email' #Username

    REQUIRED_FIELDS = ['full_name']

    objects = UserManage()

    def __str__(self):
        return self.email


    def get_full_name(self):
        fullname = self.full_name
        return fullname

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
