from django.urls import path
from .views import GetPhoto, PhotoUploadView

app_name = 'photoupload'

urlpatterns = [
    path('upload/', PhotoUploadView.as_view()),
    path('uploads/<int:pk>', GetPhoto.as_view()),
]