from django.db import models

# Create your models here.

from django.db import models

class Borrower(models.Model):
    borrower_name = models.CharField(max_length=100)
    borrower_address = models.CharField(max_length=200)
    borrower_contact_number = models.CharField(max_length=15)
    borrower_email = models.EmailField()
    borrower_credit_score = models.IntegerField()
    borrower_employment_status = models.CharField(max_length=50)

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    loan_term = models.IntegerField()
    loan_status = models.CharField(max_length=50)
    loan_start_date = models.DateField()
    loan_end_date = models.DateField()
    repayment_method = models.CharField(max_length=50)

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

class Admin(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_username = models.CharField(max_length=50)
    admin_password = models.CharField(max_length=50)