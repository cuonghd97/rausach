import json
from datetime import datetime

from django.shortcuts import render
from django.contrib.auth import decorators
from django.http import HttpResponse, JsonResponse

from General.decorators import is_admin
from Store.models import *

# Create your views here.

THEM_THANH_CONG = {"status": "success", "messages": 'Thêm thành công'}
SUA_THANH_CONG = {"status": "success", "messages": 'Sửa thành công'}
LOI = {"status": "error", "messages": 'Lỗi'}
XOA_THANH_CONG = {"status": "success", "messages": 'Xóa thành công'}


def base(request):
    user = request.user
    return render(request, 'Store/layouts/base.html', {"user": user})

# Json tỉnh
@decorators.login_required(login_url='/auth/login/')
def data_tinh(request):
    json_data = open('static/data/province.json')
    data = json.load(json_data)

    return JsonResponse(data, safe=False)


# Json huyện
@decorators.login_required(login_url='/auth/login/')
def data_huyen(request):
    json_data = open('static/data/district.json')
    data = json.load(json_data)

    return JsonResponse(data, safe=False)


# Quản lý sản phẩm trong cửa hàng
@decorators.login_required(login_url='/auth/login/')
@is_admin
def san_pham(request):
    return render(request, 'Store/categories/products.html')
# Data sản phẩm


def data_anh_sp(request, id):
    anh = HinhAnhSP.objects.filter(san_pham=id).values()
    return JsonResponse(list(anh), safe=False)


def data_san_pham(request):
    san_pham = SanPham.objects.all()

    data = []
    i = 1
    for sp in san_pham:
        obj = {}
        obj.update({'no': i})
        obj.update({'id': sp.id})
        obj.update({'ten_san_pham': sp.ten_san_pham})
        obj.update({'ngay_them': sp.ngay_them})
        obj.update({'gia_von': sp.gia_von})
        obj.update({'gia_ban': sp.gia_ban})
        obj.update({'ton_kho': sp.ton_kho})
        obj.update({'is_active': sp.is_active})
        obj.update({'so_luong': sp.so_luong})
        obj.update({'mo_ta': sp.mo_ta})
        obj.update({'loai_hang': sp.loai_hang.ten_loai})
        obj.update({'id_loai_hang': sp.loai_hang.id})
        obj.update({'nha_cung_cap': sp.nha_cung_cap.ten})
        obj.update({'id_nha_cung_cap': sp.nha_cung_cap.id})
        obj.update({'khuyen_mai': sp.khuyen_mai})
        obj.update({"anh": str(sp.avt)})
        i += 1

        data.append(obj)
    return JsonResponse(data, safe=False)


# Post sản phẩm
@decorators.login_required(login_url='/auth/login/')
@is_admin
def post_san_pham(request):
    if request.method == 'POST':
        images = request.FILES.getlist('anh')
        ten_san_pham = request.POST.get('ten_san_pham')
        gia_von = request.POST.get('gia_von')
        gia_ban = request.POST.get('gia_ban')
        so_luong = request.POST.get('so_luong')
        loai_hang = request.POST.get('loai_hang')
        nha_cung_cap = request.POST.get('nha_cung_cap')
        khuyen_mai = request.POST.get('khuyen_mai')
        mo_ta = request.POST.get('mo_ta')
        avt = request.FILES.get('image_avt')
        is_add = request.POST.get('is_add')
        id_sp = request.POST.get('id')
        is_edit = request.POST.get('is_edit')
        is_delete = request.POST.get('is_delete')
        is_active = request.POST.get('is_active')
        if is_add != None:
            try:
                san_pham = SanPham()
                san_pham.ten_san_pham = ten_san_pham
                san_pham.gia_von = gia_von
                san_pham.gia_ban = gia_ban
                san_pham.so_luong = so_luong
                san_pham.loai_hang = LoaiHang.objects.get(pk=loai_hang)
                san_pham.nha_cung_cap = NhaCungCap.objects.get(pk=nha_cung_cap)
                san_pham.mo_ta = mo_ta
                san_pham.ton_kho = so_luong
                san_pham.avt = avt
                san_pham.save()
                id_sp = san_pham.id
                for image in images:
                    anh_sp = HinhAnhSP()
                    anh_sp.san_pham = SanPham.objects.get(pk=id_sp)
                    anh_sp.hinh_anh = image
                    anh_sp.save()
            except:
                pass
        if is_edit != None:
            try:
                san_pham = SanPham.objects.get(pk=id_sp)
                san_pham.ten_san_pham = ten_san_pham
                san_pham.gia_von = gia_von
                san_pham.gia_ban = gia_ban
                san_pham.so_luong = so_luong
                san_pham.loai_hang = LoaiHang.objects.get(pk=loai_hang)
                san_pham.khuyen_mai = khuyen_mai
                print(khuyen_mai)
                san_pham.nha_cung_cap = NhaCungCap.objects.get(pk=nha_cung_cap)
                san_pham.mo_ta = mo_ta
                san_pham.ton_kho = so_luong
                if avt != None:
                    san_pham.avt = avt
                san_pham.is_active = is_active
                san_pham.save()
                if images != []:
                    HinhAnhSP.objects.filter(san_pham=id_sp).delete()
                    for image in images:
                        anh_sp = HinhAnhSP()
                        anh_sp.san_pham = SanPham.objects.get(pk=id_sp)
                        anh_sp.hinh_anh = image
                        anh_sp.save()
            except:
                pass
        if is_delete != None:
            try:
                SanPham.objects.get(pk=id_sp).delete()
                return JsonResponse(XOA_THANH_CONG)
            except:
                return JsonResponse(LOI)
        return JsonResponse({})
    return JsonResponse({})

# Quản lý loại hàng


@decorators.login_required(login_url='/auth/login/')
@is_admin
def loai_hang(request):
    return render(request, 'Store/categories/categories.html')

# Data loại hàng


def data_loai_hang(request):
    loai_hang = LoaiHang.objects.all()
    data = []
    i = 1
    for item in loai_hang:
        obj = {}
        obj.update({'no': i})
        obj.update({'id': item.id})
        obj.update({'ten_loai': item.ten_loai})
        i += 1

        data.append(obj)

    return JsonResponse(data, safe=False)

# Post loại hàng


@decorators.login_required(login_url='/auth/login/')
@is_admin
def post_loai_hang(request):
    if request.method == 'POST':
        ten_loai = request.POST.get('ten_loai')
        is_add = request.POST.get('is_add')
        is_edit = request.POST.get('is_edit')
        id_loai_hang = request.POST.get('id_loai_hang')
        is_delete = request.POST.get('is_delete')

        if is_add != None:
            loai_hang = LoaiHang()
            loai_hang.ten_loai = ten_loai
            loai_hang.save()

            return JsonResponse(THEM_THANH_CONG)
        if is_edit != None:
            loai_hang = LoaiHang.objects.get(pk=id_loai_hang)
            loai_hang.ten_loai = ten_loai
            loai_hang.save()
            return JsonResponse(SUA_THANH_CONG)
        if is_delete != None:
            loai_hang = LoaiHang.objects.get(pk=id_loai_hang).delete()
            return JsonResponse(XOA_THANH_CONG)
    return JsonResponse({})


#  Nhà cung cấp
@decorators.login_required(login_url='/auth/login/')
@is_admin
def nha_cung_cap(request):
    return render(request, 'Store/providers/providers.html')

# Data nhà cung cấp


def data_nha_cung_cap(request):
    nha_cung_cap = NhaCungCap.objects.all()

    data = []
    i = 1
    for ncc in nha_cung_cap:
        obj = {}
        obj.update({'no': i})
        obj.update({'id': ncc.id})
        obj.update({'ten_nha_cung_cap': ncc.ten})
        obj.update({'so_dien_thoai': ncc.sdt})
        obj.update({'email': ncc.email})
        obj.update({'dia_chi': ncc.dia_chi})
        obj.update({'huyen': ncc.huyen})
        obj.update({'tinh': ncc.tinh})
        obj.update({'is_active': ncc.is_active})
        obj.update({'mo_ta': ncc.mo_ta})
        obj.update({'created_at': ncc.created_at})

        data.append(obj)
        i += 1

    return JsonResponse(data, safe=False)

# Post dữ liệu nhà cung cấp


@decorators.login_required(login_url='/auth/login/')
@is_admin
def post_nha_cung_cap(request):
    if request.method == 'POST':
        ten_nha_cung_cap = request.POST.get('ten_nha_cung_cap')
        dia_chi = request.POST.get('dia_chi')
        tinh = request.POST.get('tinh')
        huyen = request.POST.get('huyen')
        email = request.POST.get('email')
        sdt = request.POST.get('sdt')
        is_add = request.POST.get('is_add')
        is_edit = request.POST.get('is_edit')
        id_ncc = request.POST.get('id_ncc')
        mo_ta = request.POST.get('mo_ta')
        is_active = request.POST.get('is_active')
        is_delete = request.POST.get('is_delete')

        if is_add != None:
            try:
                ncc = NhaCungCap()
                ncc.ten = ten_nha_cung_cap
                ncc.sdt = sdt
                ncc.email = email
                ncc.dia_chi = dia_chi
                ncc.tinh = tinh
                ncc.huyen = huyen
                ncc.mo_ta = mo_ta
                ncc.save()
                return JsonResponse(THEM_THANH_CONG)
            except:
                return JsonResponse(LOI)

        if is_edit != None:
            try:
                ncc = NhaCungCap.objects.get(pk=id_ncc)
                ncc.ten = ten_nha_cung_cap
                ncc.sdt = sdt
                ncc.email = email
                ncc.dia_chi = dia_chi
                ncc.tinh = tinh
                ncc.is_active = is_active
                ncc.huyen = huyen
                ncc.mo_ta = mo_ta
                ncc.save()

                return JsonResponse(SUA_THANH_CONG)
            except:
                return JsonResponse(LOI)
        if is_delete != None:
            try:
                ncc = NhaCungCap.objects.get(pk=id_ncc).delete()

                return JsonResponse(XOA_THANH_CONG)
            except:
                return JsonResponse(LOI)

    else:
        return JsonResponse(LOI)


# Quản lý nhân viên trong cửa hàng
@decorators.login_required(login_url='/auth/login/')
@is_admin
def nhan_vien(request):
    return render(request, 'Store/staff/staff.html')


# Data nhân viên
@decorators.login_required(login_url='/auth/login/')
@is_admin
def data_nhan_vien(request):
    users = MyUsers.objects.filter(role__in=[1, 2])
    data = []
    i = 1
    for nhan_vien in users:
        obj = {}
        obj.update({'no': i})
        obj.update({'id': nhan_vien.id})
        obj.update({'huyen': nhan_vien.huyen})
        obj.update({'tinh': nhan_vien.tinh})
        obj.update({'dia_chi': nhan_vien.dia_chi})
        obj.update({'ho_ten': nhan_vien.ho_ten})
        obj.update({'ngay_sinh': nhan_vien.ngay_sinh})
        obj.update({'luong': nhan_vien.luong})
        obj.update({'sdt': nhan_vien.sdt})
        obj.update({'gioi_tinh': nhan_vien.gioi_tinh})
        obj.update({'created_at': nhan_vien.created_at})
        obj.update({'role': nhan_vien.role})
        obj.update({'username': nhan_vien.username})
        obj.update({'is_active': nhan_vien.is_active})
        obj.update({'email': nhan_vien.email})
        obj.update({'avatar': str(nhan_vien.avatar)})

        i += 1
        data.append(obj)
    return JsonResponse(data, safe=False)

# Post dữ liệu nhân viên
@decorators.login_required(login_url='/auth/login/')
@is_admin
def post_nhan_vien(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        ten_nhan_vien = request.POST.get('ten_nhan_vien')
        gioi_tinh = request.POST.get('gioi_tinh')
        email = request.POST.get('email')
        sdt = request.POST.get('sdt')
        address = request.POST.get('address')
        tinh = request.POST.get('tinh')
        huyen = request.POST.get('huyen')
        role = request.POST.get('role')
        ngay_sinh = request.POST.get('ngay_sinh')
        luong = request.POST.get('luong')
        anh = request.FILES.get('anh')
        is_add = request.POST.get('is_add')
        is_edit = request.POST.get('is_edit')
        id_staff = request.POST.get('id')
        is_active = request.POST.get('is_active')
        is_delete = request.POST.get('is_delete')
        if is_add != None:
            try:
                user = MyUsers()
                user.username = username
                user.gioi_tinh = gioi_tinh
                user.ho_ten = ten_nhan_vien
                user.email = email
                user.sdt = sdt
                user.set_password(username)
                user.dia_chi = address
                user.tinh = tinh
                user.huyen = huyen
                user.role = role
                user.ngay_sinh = datetime.strptime(ngay_sinh, '%Y-%m-%d')
                user.luong = luong
                user.avatar = anh
                user.is_active = 1
                user.save()
                return JsonResponse(THEM_THANH_CONG)
            except:
                return JsonResponse(LOI)
        elif is_edit != None:
            try:
                user = MyUsers.objects.get(pk=id_staff)
                user.username = username
                user.ho_ten = ten_nhan_vien
                user.gioi_tinh = gioi_tinh
                user.email = email
                user.sdt = sdt
                user.set_password(username)
                user.dia_chi = address
                user.tinh = tinh
                user.huyen = huyen
                user.role = role
                user.ngay_sinh = datetime.strptime(ngay_sinh, '%Y-%m-%d')
                user.luong = luong
                if anh != None:
                    user.avatar = anh
                user.is_active = is_active
                user.save()

                return JsonResponse(SUA_THANH_CONG)
            except:
                return JsonResponse(LOI)
        elif is_delete != None:
            try:
                MyUsers.objects.get(pk=id_staff).delete()
                return JsonResponse(XOA_THANH_CONG)
            except:
                return JsonResponse(LOI)
        return JsonResponse({}, safe=False)
    return JsonResponse({}, safe=False)

# Quản lý người dùng
@decorators.login_required(login_url='/auth/login/')
@is_admin
def nguoi_dung(request):
    return render(request, 'Store/Customers/customers.html')

# Data người dùng
@decorators.login_required(login_url='/auth/login/')
@is_admin
def data_nguoi_dung(request):
    users = MyUsers.objects.filter(role=3)
    data = []
    i = 1
    for nguoi_dung in users:
        obj = {}
        obj.update({'no': i})
        obj.update({'id': nguoi_dung.id})
        obj.update({'huyen': nguoi_dung.huyen})
        obj.update({'tinh': nguoi_dung.tinh})
        obj.update({'dia_chi': nguoi_dung.dia_chi})
        obj.update({'ho_ten': nguoi_dung.ho_ten})
        obj.update({'ngay_sinh': nguoi_dung.ngay_sinh})
        obj.update({'sdt': nguoi_dung.sdt})
        obj.update({'gioi_tinh': nguoi_dung.gioi_tinh})
        obj.update({'created_at': nguoi_dung.created_at})
        obj.update({'role': nguoi_dung.role})
        obj.update({'username': nguoi_dung.username})
        obj.update({'is_active': nguoi_dung.is_active})
        obj.update({'email': nguoi_dung.email})
        obj.update({'avatar': str(nguoi_dung.avatar)})

        i += 1
        data.append(obj)
    return JsonResponse(data, safe=False)

# Post dữ liệu nhân viên
@decorators.login_required(login_url='/auth/login/')
@is_admin
def post_nguoi_dung(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        ten_nguoi_dung = request.POST.get('ten_nguoi_dung')
        gioi_tinh = request.POST.get('gioi_tinh')
        email = request.POST.get('email')
        sdt = request.POST.get('sdt')
        address = request.POST.get('address')
        tinh = request.POST.get('tinh')
        huyen = request.POST.get('huyen')
        role = request.POST.get('role')
        ngay_sinh = request.POST.get('ngay_sinh')
        anh = request.FILES.get('anh')
        is_add = request.POST.get('is_add')
        is_edit = request.POST.get('is_edit')
        id_staff = request.POST.get('id')
        is_active = request.POST.get('is_active')
        is_delete = request.POST.get('is_delete')
        if is_add != None:
            try:
                user = MyUsers()
                user.username = username
                user.gioi_tinh = gioi_tinh
                user.ho_ten = ten_nguoi_dung
                user.email = email
                user.sdt = sdt
                user.set_password(username)
                user.dia_chi = address
                user.tinh = tinh
                user.huyen = huyen
                user.role = role
                user.ngay_sinh = datetime.strptime(ngay_sinh, '%Y-%m-%d')
                user.avatar = anh
                user.is_active = 1
                user.save()
                return JsonResponse(THEM_THANH_CONG)
            except:
                return JsonResponse(LOI)
        elif is_edit != None:
            try:
                user = MyUsers.objects.get(pk=id_staff)
                user.username = username
                user.ho_ten = ten_nguoi_dung
                user.gioi_tinh = gioi_tinh
                user.email = email
                user.sdt = sdt
                user.set_password(username)
                user.dia_chi = address
                user.tinh = tinh
                user.huyen = huyen
                user.role = role
                user.ngay_sinh = datetime.strptime(ngay_sinh, '%Y-%m-%d')
                if anh != None:
                    user.avatar = anh
                user.is_active = is_active
                user.save()

                return JsonResponse(SUA_THANH_CONG)
            except:
                return JsonResponse(LOI)
        elif is_delete != None:
            try:
                MyUsers.objects.get(pk=id_staff).delete()
                return JsonResponse(XOA_THANH_CONG)
            except:
                return JsonResponse(LOI)
        return JsonResponse({}, safe=False)
    return JsonResponse({}, safe=False)


# Hóa đơn
@decorators.login_required(login_url='/auth/login/')
@is_admin
def hoa_don(request):
    if request.method == 'POST':
        id_invoice = request.POST.get('id_invoice')
        is_paid = request.POST.get('is_paid')
        print(request.POST)
        if is_paid != None:
            try:
                hoa_don = HoaDon.objects.get(pk=id_invoice)
                if hoa_don.is_paid == 0:
                    hoa_don.is_paid = 1
                    hoa_don.save()
                    chi_tiet_hoa_don = ChiTietHoaDon.objects.filter(
                        hoa_don=hoa_don)

                    for hang in chi_tiet_hoa_don:
                        san_pham = SanPham.objects.get(pk=hang.san_pham.id)
                        san_pham.ton_kho = san_pham.ton_kho - hang.so_luong_mua
                        san_pham.save()
                    return JsonResponse(THEM_THANH_CONG)
                else:
                    return JsonResponse({'status': 'paided'})
            except:
                return JsonResponse(LOI)

    return render(request, 'Store/transfer/invoices.html')


# Data hóa đơn
@decorators.login_required(login_url='/auth/login/')
@is_admin
def data_hoa_don(request):
    hoa_don = HoaDon.objects.all().order_by('-created_at')
    data = []
    i = 1

    for hd in hoa_don:
        obj = {}
        obj.update({'no': i})
        obj.update({'id': hd.id})
        if hd.nguoiTao:
            obj.update({'nguoi_tao': hd.nguoiTao.ho_ten})
        else:
            obj.update({'nguoi_tao': ''})
        obj.update({'id_trang_thai': hd.trang_thai.id})
        obj.update({'trang_thai': hd.trang_thai.mo_ta})
        # obj.update({'ngay_lap': hd.ngay_lap})
        obj.update({'thoi_gian_lap': hd.created_at.strftime('%H:%M')})
        obj.update({'ghi_chu': hd.ghi_chu})
        obj.update({'khach_hang': hd.ten_khach_hang})

        i += 1
        data.append(obj)

    return JsonResponse(data, safe=False)


def chi_tiet_hoa_don(request, id):
    hang = ChiTietHoaDon.objects.filter(hoa_don=id)
    hoa_don = HoaDon.objects.get(pk=id)
    user = request.user
    thanh_tien = 0
    i = 1
    data = []
    for item in hang:
        obj = {}
        obj.update({'no': i})
        obj.update({'ten_san_pham': item.san_pham.ten_san_pham})
        obj.update({'gia_ban': item.san_pham.gia_ban})
        obj.update({'so_luong_mua': item.so_luong_mua})
        obj.update({'thanh_tien': int(item.san_pham.gia_ban)
                    * int(item.so_luong_mua)})

        thanh_tien += int(item.san_pham.gia_ban) * int(item.so_luong_mua)
        data.append(obj)
    response = {}
    response.update({'ma_hoa_don': hoa_don.id})
    response.update({'ngay_tao': hoa_don.ngay_lap})
    response.update({'thanh_tien': thanh_tien})
    response.update({'data': data})
    response.update({'nguoi_tao': user.ho_ten})
    response.update({'khach_hang': hoa_don.ten_khach_hang})
    return JsonResponse(response, safe=False)

# Bán hàng


def ban_hang(request):
    return render(request, 'Store/sale/sale.html')


def data_trang_thai(request):
    trang_thai = TrangThaiHoaDon.objects.all().values()

    return JsonResponse(list(trang_thai), safe=False)