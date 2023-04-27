from django.contrib import admin

from users.models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Admin)
admin.site.register(Client)