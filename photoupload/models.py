from django.db import models

# Create your models here.

class PhotoModel(models.Model):
    image = models.ImageField(upload_to='media/')
    url = models.CharField(max_length=255)
    # url = models.CharField(max_length=255)
    # class Meta:
        
    
    def __str__(self):
        return str(self.image)
    
