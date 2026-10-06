from django.contrib import admin
from .models import Service, ServiceAdmin
admin.site.register(Service, ServiceAdmin)