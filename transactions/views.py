from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import CustomUser
from .models import Loan
from .serializers import LoanSerializer
from rest_framework import generics, permissions

# from rest_framework import generics, permissions

# This is gr8
class CreateLoanView(generics.CreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]




class LoanListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, id):
        
        
        user=CustomUser.objects.get(id=id)
        query =Loan.objects.filter(borrower=user)
        serializer=LoanSerializer(query,many=True)
        return  Response(serializer.data)
    
