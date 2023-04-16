from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import CustomUserRegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.

class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        nom = request.data.get('nom')
        prenom = request.data.get('prenom')
        post = request.data.get('post')
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'id':user.id,
                'nom':user.nom,
                'prenom':user.prenom,
                'post':user.post,
                'telephone':user.phone,
                'nni':user.nni,
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            },status=200)
        else:
            return Response({
                             'message':'Check your credentials'
                            }, status= 401) 
    
    



class CustomUserRegisterView(generics.CreateAPIView):
    
    
    model = get_user_model()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status= Response.status_code)


