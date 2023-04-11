from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/',include('authtokens.urls', namespace="authtokens")), 
    path('transaction/',include('transactions.urls', namespace="transactions")), 
    path('users/',include('users.urls', namespace="users")), 
]

urlpatterns += staticfiles_urlpatterns()