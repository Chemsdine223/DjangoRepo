from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.response import Response
from users.models import Client
from users.serializers import ClientRegisterSerializer, ClientRegisterSerializer, UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


# Create your views here.

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
        
        # nom = request.data.get('nom')
        # prenom = request.data.get('prenom')
        # post = request.data.get('post')
        phone = request.data.get('phone')
        password = request.data.get('password')
        user = authenticate(request, phone=phone, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            # image = ''
            # if user.profile_image.url is not None:
            #     image = user.profile_image.url
            return Response({
                'id':user.id,
                'nom':user.nom,
                'prenom':user.prenom,
                'post':user.post,
                'telephone':user.phone,
                'nni':user.nni,
                # 'profile_image':image,
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            },status=Response.status_code)
        else:
            return Response({
                             'message':'Check your credentials'
                            }, status= 401) 
    
    



class ClientRegisterView(generics.CreateAPIView):
    
    
    model = get_user_model()
    serializer_class = ClientRegisterSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status= Response.status_code)


