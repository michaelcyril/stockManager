from django.forms import model_to_dict
from django.shortcuts import render,redirect,reverse,HttpResponse
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

def employee_form(request):
    if request.method == "POST":
        data = request.POST
        forms = EmployeeForm(data)
        if forms.is_valid():
            forms.save()
            return redirect('http://127.0.0.1:8000/employee_form')
    return render(request, 'employee_form.html')

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

#IT SAVE WITHOUT UPDATE THE STOCK

# def SellingView(request):
#     if request.method=="POST":
#         data=request.POST
#         forms=SalesForm(data)
#         if forms.is_valid():
#             forms.save()
#             return redirect('http://127.0.0.1:8000/selling')
#     product=Stock.objects.all()
#     seller=Employee.objects.all()
#     context={
#         'products':product,
#         'sellers':seller
#
#     }
#     return render(request,'selling_form.html',context)
#





#REDIRECT TO SHIFT WITH SOME MESSAGES
# def save_form(request, *args, **kwargs):
#     # all goes well
#     message = _("form for customer xyz was successfully updated...")
#     request.user.message_set.create(message=message)
#     return redirect('list_view')
#
#
# def list_view(request, *args, **kwargs):
#     # Render page
#     # Template for list_view:
#     {% for message in messages %}

#     { % endfor %}



def SellingView(request):

    if request.method=="POST":
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
            return redirect('http://127.0.0.1:8000/selling')
        new_quantity = stock_before[0]['quantity'] - int(q_red)

        if stock_before[0]['quantity'] >= int(q_red):
            new_stock=Stock.objects.get(id=pro_id)
            new_stock.quantity=new_quantity
            new_stock.save()
            form=SalesForm(data)
            # if data.is_valid():
            form.save()
            #some messages
            # return redirect('product_form')
            #some messages
            return redirect('http://127.0.0.1:8000/selling')

        #some messages
        return redirect('http://127.0.0.1:8000/selling')

    product=Stock.objects.all()
    seller=Employee.objects.all()
    context={
        'products':product,
        'sellers':seller

    }
    return render(request,'selling_form.html',context)
