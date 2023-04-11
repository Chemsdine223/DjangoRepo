from rest_framework import serializers
from .models import Loan

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'borrower', 'loan_amount', 'interest_rate', 'loan_status', 'loan_start_date', 'loan_end_date', 'repayment_method']
