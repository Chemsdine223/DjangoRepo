from django.contrib import admin
# from transactions.models import Adminstrator

from users.models import *

# Register your models here.
admin.site.register(CustomUser)
# admin.site.register(Adminstrator)
admin.site.register(Client)