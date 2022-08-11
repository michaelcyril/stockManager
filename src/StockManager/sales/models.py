from django.db import models

# Create your models here.
class Employee(models.Model):
    username=models.CharField(max_length=30)
    phone_no=models.CharField(max_length=10)
    is_still_aactive=models.BooleanField(default=True)
    def __str__(self):
        return self.username

class Stock(models.Model):
    product=models.CharField(max_length=30)
    quantity=models.IntegerField()
    description=models.TextField()
    buyying_price=models.DecimalField(max_digits=10,decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by=models.ForeignKey(Employee,on_delete=models.CASCADE)
    created_ad=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.product

class Sales(models.Model):
    product=models.ForeignKey(Stock,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    selling_price=models.DecimalField(max_digits=10,decimal_places=2)
    created_by=models.ForeignKey(Employee,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    def total(self):
        return self.quantity*self.selling_price

