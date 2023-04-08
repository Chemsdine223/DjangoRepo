from django.urls import path
from users.views import CustomUserRegisterView, UserLoginView

app_name = "users"

urlpatterns = [
    path("register/",CustomUserRegisterView.as_view(),name = "register"),   
    path('login/', UserLoginView.as_view(), name='login'),
]
