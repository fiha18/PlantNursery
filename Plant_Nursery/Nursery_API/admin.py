from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Plants)
admin.site.register(Users)
admin.site.register(Nursery)
admin.site.register(NurseryPlant)
admin.site.register(UserPlant)