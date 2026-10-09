from django.db import models
from django.contrib import admin
class Blinkit(models.Model):
    User_Id = models.IntegerField(primary_key=True)
    User_Name = models.CharField(max_length=100)
    Mobile_Number = models.IntegerField(max_length=10)
    Email = models.EmailField()
    Address = models.TextField()
    Order_Id = models.IntegerField()
    Order_Date = models.DateField()
    Product_Name = models.CharField(max_length=100)
    Delivery_Date = models.DateField()
class BlinkitAdmin(admin.ModelAdmin):
    list_display=["User_Id","User_Name","Mobile_Number","Email","Address","Order_Id","Order_Date","Product_Name","Delivery_Date"]

