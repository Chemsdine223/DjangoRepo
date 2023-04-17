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
    def post(self, request, *args, **kwargs):
        # Check if the user already has a loan
        user_loans = Loan.objects.filter(user=request.user, is_active=True)
        if user_loans.exists():
            return Response({'error': 'You already have an active loan.'}, status=400)

        # Create the loan object
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=201)




class LoanListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request, id):
        
        
        user=CustomUser.objects.get(id=id)
        query =Loan.objects.filter(borrower=user)
        serializer=LoanSerializer(query,many=True)
        return  Response(serializer.data)
        
