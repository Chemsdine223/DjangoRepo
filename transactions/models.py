from django.db import models

# Create your models here.

from django.db import models

from users.models import CustomUser

class Loan(models.Model):
    borrower = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_status = models.CharField(max_length=50)
    loan_start_date = models.DateField()
    loan_end_date = models.DateField()
    repayment_method = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.borrower.nni)