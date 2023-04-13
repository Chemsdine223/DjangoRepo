from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin

from users.managers import CustomUserManager 

# # Create your models here.
# class Loan(models.Model):
#     loan_id = models.CharField(max_length=200)
#     montant = models.DecimalField(max_digits=20, decimal_places=3)
#     raison = models.CharField(max_length=255)
#     # raison = models.ImageField()
    

    

class CustomUser(AbstractBaseUser,PermissionsMixin):
    phone = models.CharField(unique=True, max_length=8)
    nni = models.CharField(unique=True, max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = CustomUserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = [
        'nni',
        ]
    
    
    # def __str__(self):
    #     return self.phone
    