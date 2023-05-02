from django.urls import path
from .views import *

app_name = 'transactions'

urlpatterns = [
    path('loans/', CreateLoanView.as_view(), name='create_loan'),
    path('loans/<int:id>', LoanListView.as_view(), name='get_loan'),
    path('bankLoans/<int:id>', GetBankLoansListView.as_view(), name='get_loan_by_bank'),
]