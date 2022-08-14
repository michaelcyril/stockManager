from django.urls import path
from .views import sign_up,product_list,product_form,all_sales_report,testpage,print_view,employee_form,daily_sales,SellingView
app_name='sales'

urlpatterns = [
    path('product_list',product_list),
    path('product_form',product_form),
    path('all_sales_report',all_sales_report),
    path('signin',testpage),
    path('print',print_view),
    path('employee_form', employee_form),
    path('daily_sales',daily_sales),
    path('selling',SellingView),
]
