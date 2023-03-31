from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from users.managers import CustomUserManager 

# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone = models.BigIntegerField(unique=True)
    nni = models.BigIntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = [
        'nni',
        ]
    def __str__(self):
        return self.phone
    