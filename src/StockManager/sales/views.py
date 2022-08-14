from django.shortcuts import render,redirect,reverse
from .forms import StockForm,SalesForm,EmployeeForm
from .models import Sales,Stock,Employee
from datetime import datetime
from django.db.models import Sum
# Create your views here.
def testpage(request):
    return render(request,'base.html')

def sign_up(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'pages_signin.html')
    return render(request,'pages-signup.html')

def sign_in(request):
    if request.method=='POST':
        pass

def product_list(request):
    data=Stock.objects.all()
    print(data)

    context={
        'data':data
        # 'sum':sum

    }
    return render(request,'product_list.html',context)


def all_sales_report(request):
    data=Sales.objects.all()
    print(data)
    total = 0
    for instance in data:
        d=int(instance.total())
        total += d


    context={
        'data':data,
        'sum':total

    }

    return render(request,'all_sales_report.html',context)
def product_form(request):
    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    if request.method=='POST':
        data=StockForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect(reverse('product_form'))
    return render(request,'product_form.html',context)
def print_view(request):
    return render(request,'pages-invoice-print.html')

def employee_form(request):
    return render(request,'employee_form.html')

def daily_sales(request):
    today = datetime.today()

    year = today.year
    month = today.month
    day = today.day
    dai=today
    date_str = dai.strftime("%d-%m-%Y")

    data = Sales.objects.filter(created_at__year=year,
                               created_at__month=month, created_at__day=day)
    print(data)
    total = 0
    for instance in data:
        d=int(instance.total())
        total += d

    context={
        'data':data,
        'day':date_str,
        'sum':total
    }
    return render(request,'daily_sales.html',context)

def SellingView(request):
    return render(request,'selling_form.html')
