from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, decorators, logout, get_user
from .models import MyUsers
from ManageStore import models
from django.shortcuts import redirect
from django.contrib import messages
import uuid

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
        MyUsers = authenticate(username=username, password=password)
        if MyUsers is None:
            messages.warning(request, "Sai tên đăng nhập hoặc mật khẩu")
            return render(request, 'login.html')
        login(request, MyUsers)
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

# Nhận dữ liệu khi thêm sản phẩm
def get_data_add_product(request):
    if request.method == 'POST':
        try:
            hang_hoa = models.HangHoa()
            hang_hoa.maHang = request.POST.get('masanpham')
            hang_hoa.tenHang = request.POST.get('tensanpham')
            hang_hoa.giaVon = request.POST.get('giavon')
            hang_hoa.giaBan = request.POST.get('giaban')
            hang_hoa.tonKho = request.POST.get('tonkho')
            hang_hoa.trangThai = request.POST.get('trangthai')
            hang_hoa.save()
    
            listImage = request.FILES.getlist('image')
            for item in listImage:
                img = models.Anh()
                img.hangHoa = hang_hoa
                img.path = item
                img.save()
            messages.success(request, 'Thêm thành công')
            return redirect('ManageStore:products')
        except:
            messages.success(request, 'Thêm không thành công')
            return redirect('ManageStore:products')
    else:
        messages.warning(request, 'Không phải phương thức POST')
        return redirect('ManageStore:products')

# Data products
def data_product(request):
    products = models.HangHoa.objects.all()
    data = []
    i = 1
    for product in products:
        item = {}
        item.update({'no': i})
        item.update({'id': product.id})
        item.update({'ma_hang': product.maHang})
        item.update({'ten_hang': product.tenHang})
        item.update({'ngay_nhap': product.ngayNhap.strftime('%Y-%m-%d')})
        item.update({'gia_ban': product.giaBan})
        item.update({'gia_von': product.giaVon})
        item.update({'trang_thai': product.trangThai})
        item.update({'mo_ta': product.moTa})

        i += 1
        
        data_image = []
        images = models.Anh.objects.filter(hangHoa = product.id)
        for image in images:
            img = {}
            img.update({'path': str(image.path)})
            data_image.append(img)
        
        item.update({'anh': data_image})

        data.append(item)
    return JsonResponse(data, safe=False)