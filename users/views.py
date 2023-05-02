from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.exceptions import AuthenticationFailed 
from rest_framework.response import Response
from rest_framework.decorators import *
# from transactions.models import Loan

from users.models import Client
from users.serializers import ClientRegisterSerializer, ClientRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.

# Users authentication and registration

class AuthenticatedUserData(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = Client.objects.get(id=id)
        except Client.DoesNotExist:
            return Response(status=404)

        user_data = {
            'id': user.id,
            'nom': user.nom,
            'prenom': user.prenom,
            'post': user.post,
            'phone': user.phone,
            'nni': user.nni,

        }
        return Response(user_data)

class ClientLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        password = request.data.get('password')
        client = authenticate(request, phone=phone, password=password)
        if client is not None:
            refresh = RefreshToken.for_user(client)
            return Response({
                'id':client.id,
                'nom':client.nom,
                'prenom':client.prenom,
                'post':client.post,
                'telephone':client.phone,
                'nni':client.nni,
                # 'profile_image':image,
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            },status=Response.status_code)
        else:
            return Response({
                             'message':'Check your credentials'
                            }, status= 401) 

class ClientRegisterView(generics.CreateAPIView):
    
    model = Client
    serializer_class = ClientRegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status= Response.status_code)


# Admins authentication:

# class AadminLoginView(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
        
#         phone = request.data['phone']
#         password = request.data['password']
#         admin = Adminstrator.objects.filter(phone=phone).first()
#         if admin is None:
#             raise AuthenticationFailed('check password')
#         if admin.check_password(password):
            
#             refresh = RefreshToken.for_user(admin)
#             return Response({
#                 'id':admin.id,
#                 'nom':admin.nom,
#                 'prenom':admin.prenom,
#                 'post':admin.post,
#                 'bank':admin.bank,
#                 'telephone':admin.phone,
#                 'nni':admin.nni,
#                 'refresh':str(refresh),
#                 'access':str(refresh.access_token)
#             },status=Response.status_code)
#         else:
#             return Response({
#                              'message':'Check your credentials'
#                             }, status= 401) 


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def getLoan(request):
#     if request.method == 'GET':
        
#         loan = Loan.objects.filter(bank = bank)
    


