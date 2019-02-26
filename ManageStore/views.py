from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, decorators, logout, get_user
from .models import NhanVien
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

@decorators.login_required(login_url='/login/')
def Base(request):
  if not request.user.is_authenticated:
    messages.warning(request, "Sai ten dang nhap hoac mat khau")
    return render(request, 'login.html')
  return render(request, 'base.html')

def Direct(request):
  return redirect("ManageStore:login")

# Dashboard
def Dashboard(request):
  return render(request, 'dashboard.html')

# Login
class LoginClass(View):
  def get(self, request):
    return render(request, 'login.html')
  def post(self, request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    NhanVien = authenticate(username = username, password = password)
    if NhanVien is None:
      messages.warning(request, "Sai tên đăng nhập hoặc mật khẩu")
      return render(request, 'login.html')
    login(request, NhanVien)
    return redirect('ManageStore:dashboard')

# List Products
@decorators.login_required(login_url='/login/')
def products(request):
  return render(request, 'products/list-products.html')

# Set price
@decorators.login_required(login_url='/login/')
def set_price(request):
  return render(request, 'products/set-price.html')

# Inventory
@decorators.login_required(login_url='/login/')
def inventory(request):
  return render(request, 'products/inventory.html')

# Invoices
@decorators.login_required(login_url='/login/')
def invoice(request):
  return render(request, 'exchange/invoices.html')

# Purchase oroder
@decorators.login_required(login_url='/login/')
def purchase_order(request):
  return render(request, 'exchange/purchase-order.html')

# Purchase return
@decorators.login_required(login_url='/login/')
def pruchase_return(request):
  return render(request, 'exchange/purchase-return.html')

# Returns
@decorators.login_required(login_url='/login/')
def returns(request):
  return render(request, 'exchange/returns.html')

# Damage item
@decorators.login_required(login_url='/login/')
def damage_item(request):
  return render(request, 'exchange/damage-item.html')

# Cash book
@decorators.login_required(login_url='/login/')
def cash_book(request):
  return render(request, 'cashbook/cash-book.html')

# Customer
@decorators.login_required(login_url='/login/')
def customers(request):
  return render(request, 'partner/customers.html')

# Suppliers
@decorators.login_required(login_url='/login/')
def suppliers(request):
  return render(request, 'partner/suppliers.html')

# Customer report
@decorators.login_required(login_url='/login/')
def customer_report(request):
  return render(request, 'reports/customer-report.html')

# Employee report
@decorators.login_required(login_url='/login/')
def employee_report(request):
  return render(request, 'reports/employee-report.html')

# End of day report 
@decorators.login_required(login_url='/login/')
def end_of_day_report(request):
  return render(request, 'reports/end-of-day-report.html')

# Order report
@decorators.login_required(login_url='/login/')
def order_report(request):
  return render(request, 'reports/order-report.html')

# Product report 
@decorators.login_required(login_url='/login/')
def product_report(request):
  return render(request, 'reports/product-report.html')

# Sale report 
@decorators.login_required(login_url='/login/')
def sale_report(request):
  return render(request, 'reports/sale-report.html')

# Supplier report
@decorators.login_required(login_url='/login/')
def supplier_report(request):
  return render(request, 'reports/supplier-report.html')

# Logout
def UserLogout(request):
  logout(request)
  return redirect('ManageStore:login')