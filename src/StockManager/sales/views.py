from django.contrib.auth import login,logout
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password
from django.forms import model_to_dict
from django.shortcuts import render,redirect,reverse,HttpResponse
from .forms import StockForm,SalesForm,EmployeeForm
from .models import Sales,Stock,Employee
from datetime import datetime
from django.db.models import Sum
from authentication.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

#special for printing
# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


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
@login_required(login_url='http://127.0.0.1:8000/login')
def product_list(request):
    data=Stock.objects.all()
    print(data)
    total=0
    for instance in data:
        d=int(instance.expectedprofit())
        total += d

    context={
        'data':data,
        'sum':total

    }
    return render(request,'product_list.html',context)

@login_required(login_url='http://127.0.0.1:8000/login')
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
@login_required(login_url='http://127.0.0.1:8000/login')
def product_form(request):
    if request.method == "POST":
        data = request.POST
        forms = StockForm(data)
        if forms.is_valid():
            forms.save()
            return redirect('http://127.0.0.1:8000/product_form')

    emp=Employee.objects.all()
    context={
        'emp':emp
    }
    if request.method=='POST':
        data=StockForm(request.POST)
        if data.is_valid():
            data.save()
        return redirect('http://127.0.0.1:8000/product_form')
    return render(request,'product_form.html',context)
def print_view(request):
    return render(request,'pages-invoice-print.html')
@login_required(login_url='http://127.0.0.1:8000/login')
def employee_form(request):
    if request.method == "POST":
        data = request.POST
        forms = EmployeeForm(data)
        if forms.is_valid():
            forms.save()
            return redirect('http://127.0.0.1:8000/employee_form')
    return render(request, 'employee_form.html')

@login_required(login_url='http://127.0.0.1:8000/login')
def daily_sales(request):
    today = datetime.today()
    print('the user is',request.user)

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
@login_required(login_url='http://127.0.0.1:8000/login')
def daily_sales_print(request):
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
    return render(request,'pages-invoice-print.html',context)


# @login_required
def SellingView(request):

    if request.method=="POST":
        # logout(request)
        data=request.POST
        q_red=request.POST.get('quantity',False)
        pro_id=request.POST.get('product',False)
        stock_before=Stock.objects.filter(id=pro_id).values()
        #THE CODE TO CONVERT THE QUERYSET INTO DICTATIONARY
        list_result = [entry for entry in stock_before]
        print(list_result)
        print('the data are ',stock_before[0]['quantity'])
        if stock_before[0]['quantity'] == 0:
            #some messages
            sms='Idadi ya '+stock_before[0]['product']+'zimeisha.'
            message={'message':sms}
            return redirect('http://127.0.0.1:8000/selling',message)

        elif stock_before[0]['quantity'] < int(q_red):
            #some messages
            sms='Idadi ya '+str(stock_before[0]['product'])+' zimebaki '+str(stock_before[0]['quantity'])+' hauwezi kuuza '+q_red
            message={'message':sms}
            return redirect('http://127.0.0.1:8000/selling',message)

        new_quantity = stock_before[0]['quantity'] - int(q_red)

        if stock_before[0]['quantity'] >= int(q_red):
            new_stock=Stock.objects.get(id=pro_id)
            new_stock.quantity=new_quantity
            new_stock.save()
            form=SalesForm(data)
            form.save()
            return redirect('http://127.0.0.1:8000/selling')
        return redirect('http://127.0.0.1:8000/selling')

    product=Stock.objects.all()
    seller=Employee.objects.all()
    context={
        'products':product,
        'sellers':seller

    }
    return render(request,'selling_form.html',context)



def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('http://127.0.0.1:8000/daily_sales')
    return render(request,'login.html')


def logout_user(request):
    logout(request)
    # messages.info(request, "You have successfully logged out.")
    return redirect('http://127.0.0.1:8000/selling')