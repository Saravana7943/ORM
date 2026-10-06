from django.db import models
from django.contrib import admin
class Service(models.Model):
    Vehical_NO=models.CharField(primary_key=True, max_length=100)
    Vehical_Name=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    mobile=models.IntegerField()
    Address=models.TextField(max_length=100)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("Vehical_NO", "Vehical_Name", "Name", "mobile", "Address")