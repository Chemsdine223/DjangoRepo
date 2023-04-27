from datetime import datetime
from django.db import models

# Create your models here.

from django.db import models

from users.models import Admin, Client



class Bank(models.Model):
    nom = models.CharField(max_length=50)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

class Loan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank = True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, blank = True)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)
    loan_status = models.CharField(max_length=50)
    loan_start_date = models.DateField(default=datetime.now)
    loan_end_date = models.DateField()
    repayment_method = models.CharField(max_length=50)
    # bank = models.ForeignKey()
    choices = (
        ('Pending', 'Pending'),
        ('Success', 'Success'),
        ('Confirmed', 'Confirmed'),
        ('Refused', 'Refused'),
    )
    state = models.CharField(max_length=32, choices=choices, default='Pending')

    
    
    def __str__(self):
        return str(self.client.nom)
    
