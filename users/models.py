from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from users.managers import CustomUserManager 


class CustomUser(AbstractBaseUser,PermissionsMixin):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    post = models.CharField(max_length=255)
    phone = models.CharField(unique=True, max_length=8)
    nni = models.CharField(unique=True, max_length=10)
    profile_image = models.ImageField(upload_to='media/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = [
        'nni',
        'nom',
        'prenom',
        'post',
        'photo',
        'profile_image'
        ]
    
    
    def __str__(self):
        return self.nom
    