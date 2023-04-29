from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import Client, CustomUser, Client
from users.serializers import BankLoans
from .models import Bank, Loan
from .serializers import LoanSerializer
from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken



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

    def get(self,request,id):
        client=Client.objects.get(id=id)
        query =Loan.objects.filter(borrower=client)
        serializer=LoanSerializer(query,many=True)
        return  Response(serializer.data)



class BankLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        
        phone = request.data['phone']
        password = request.data['password']
        bank = Bank.objects.filter(phone=phone).first()
        if bank is None:
            raise AuthenticationFailed('check password')
        if bank.check_password(password):
            
            refresh = RefreshToken.for_user(bank)
            return Response({
                'id':bank.id,
                'nom':bank.nom,
                'prenom':bank.prenom,
                'post':bank.post,
                'telephone':bank.phone,
                'nni':bank.nni,
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            },status=Response.status_code)
        else:
            return Response({
                             'message':'Check your credentials'
                            }, status= 401) 



class GetBankLoansListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request,id):
        bank = Bank.objects.get(id=id)
        query = Loan.objects.filter(bank = bank.id)
        serializer = BankLoans(query, many = True)
        return Response(serializer.data)