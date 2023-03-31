from django.urls import path
from users.views import CustomUserRegisterView

app_name = "users"

urlpatterns = [
    path("register/",CustomUserRegisterView.as_view(),name = "register"),   
]
