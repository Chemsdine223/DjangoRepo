from django.shortcuts import render
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class CustomUserRegisterSerializer(serializers.ModelSerializer):
        
    nni = serializers.IntegerField(
        required = True,
        validators= [
            UniqueValidator(
                queryset= CustomUser.objects.all(),
                
            )
        ]
    )
    phone = serializers.IntegerField(
        required = True,
        validators= [
            UniqueValidator(
                queryset= CustomUser.objects.all(),
                
            )
        ]
    )
    
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [
            validate_password,
        ],
        style ={
            "input_type":"password",
        },
    )
    
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        validators = [
            validate_password,
        ],
        style ={
            "input_type":"password",
        },
    )
    
    class Meta:
        model = CustomUser
        fields = (
            "phone",
            "nni",
            "password",
            "password2",
            
        )
    
    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {
                    "password":"passwords must match. "
                }
            )
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            phone= validated_data["phone"],
            nni= validated_data["nni"],

        )
        user.set_password(
            validated_data["password"]
        )
        user.save()
        return user
    