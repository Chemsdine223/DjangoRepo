from django.db import models

# from users.models import CustomUser

# Create your models here.

class PhotoModel(models.Model):
    image = models.ImageField(upload_to='media/')
    url = models.CharField(max_length=255)
    # user_id = models.OneToOneField(CustomUser.id, on_delete=models.CASCADE)
    # url = models.CharField(max_length=255)
    # class Meta:
        
    
    def __str__(self):
        return str(self.url)
    
