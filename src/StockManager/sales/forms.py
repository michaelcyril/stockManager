from django import forms
from .models import Employee,Stock,Sales

class StockForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=[
            'id',
            'product',
            'quantity',
            'description',
            'buyying_price',
            'selling_price',
            'created_by',
        ]

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=[
            'id',
            'username',
            'phone_no',
            'is_still_aactive',
        ]

class SalesForm(forms.ModelForm):
    class Meta:
        model=Sales
        fields=[
            'id',
            'product',
            'quantity',
            'selling_price',
            'created_by',
        ]