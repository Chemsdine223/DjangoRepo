from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, phone,password=None, **extra_fileds):
        
        if not phone:
            raise ValueError('phone number is required')
        
        phone = phone
        user = self.model(phone=phone, **extra_fileds)
        user.set_password(password)
        user.save(self._db)
        
        return user
        
    def create_superuser(self,phone,password = None, **extra_fields):
        user = self.create_user(
            phone,
            password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user