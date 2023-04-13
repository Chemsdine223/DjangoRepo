from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/',include('authtokens.urls', namespace="authtokens")), 
    path('transaction/',include('transactions.urls', namespace="transactions")),
    path('users/',include('users.urls', namespace="users")), 
    path('photos/',include('photoupload.urls', namespace="photos"))
]

# urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

