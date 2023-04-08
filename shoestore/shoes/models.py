from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Brand (models.Model):
    name= models.CharField(max_length=222)
    description = models.CharField(max_length= 555)
    follow_brand = models.CharField(max_length=2222, blank=True)

    def __str__(self) -> str:
        return self.name

class ShoeModel(models.Model):
    name= models.CharField(max_length=222)
    brand = models.ForeignKey(Brand, blank=True, null =True,on_delete=models.CASCADE)
    description = models.CharField(max_length= 555)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length=2222, blank=True)
    shoe_available = models.BooleanField()
    star = models.FloatField()


    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    product = models.ForeignKey(ShoeModel,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.product.title
    

# class Cartmodel(models.Model):
#     user = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
#     product = models.ForeignKey(ShoeModel,max_length=200,null=True,blank=True,on_delete=models.SET_NULL)
#     created = models.DateTimeField(auto_now_add=True)
#     count = models.IntegerField(default=1,null=True,blank=True)

#     def _str_(self):
#         return self.product.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ShoeModel, on_delete=models.CASCADE)
    image_url = models.CharField(max_length = 2083, default=False)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=6, decimal_places=2)