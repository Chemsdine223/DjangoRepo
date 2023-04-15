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
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'id':user.id,
                'status': True,
                'telephone':user.phone,
                'nni':user.nni,
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            })  # replace 'home' with the name of your homepage URL pattern
        else:
            return Response({'status': False,
                             'message':'Login ou mot de passe incorrect',
                            }) 
    
    



class CustomUserRegisterView(generics.CreateAPIView):
    
    
    model = get_user_model()
    serializer_class = CustomUserRegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status= Response.status_code)


