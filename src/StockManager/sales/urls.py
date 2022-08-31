from django.urls import path
from .views import *
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
    path('login',login_user),
    path('logout',logout_user),
    # path('print',html_to_pdf_view),
]
