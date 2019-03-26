import json

from django.shortcuts import render
from django.contrib.auth import decorators
from django.http import HttpResponse, JsonResponse

from General.decorators import is_admin
from Store.models import *

# Create your views here.


def base(request):
    return render(request, 'Store/layouts/base.html')

# Json tỉnh
@decorators.login_required(login_url='/')
def data_tinh(request):
    json_data = open('static/data/province.json')
    data = json.load(json_data)

    return JsonResponse(data, safe=False)

# Json huyện
@decorators.login_required(login_url='/')
def data_huyen(request):
    json_data = open('static/data/district.json')
    data = json.load(json_data)

    return JsonResponse(data, safe=False)

# Quản lý sản phẩm trong cửa hàng
@decorators.login_required(login_url='/')
@is_admin
def san_pham(request):
    return render(request, 'Store/categories/products.html')
# Data sản phẩm


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
        obj.update({'mo_ta': sp.mo_ta})
        obj.update({'loai_hang': sp.loai_hang.ten_loai})
        obj.update({'nha_cung_cap': sp.nha_cung_cap.ten})
        i+=1

        data.append(obj)
    return JsonResponse(data, safe=False)

# Post sản phẩm
@decorators.login_required(login_url='/')
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
        mo_ta = request.POST.get('mo_ta')
        try:
            san_pham = SanPham()
            san_pham.ten_san_pham = ten_san_pham
            san_pham.gia_von = gia_von
            san_pham.gia_ban = gia_ban
            san_pham.so_luong = so_luong
            san_pham.loai_hang = LoaiHang.objects.get(pk=loai_hang)
            san_pham.nha_cung_cap = NhaCungCap.objects.get(pk=nha_cung_cap)
            san_pham.mo_ta = mo_ta
            san_pham.ton_kho =so_luong
            san_pham.save()
            id_sp = san_pham.id
            for image in images:
                anh_sp = HinhAnhSP()
                anh_sp.san_pham = SanPham.objects.get(pk=id_sp)
                anh_sp.hinh_anh = image
                anh_sp.save()
        except:
            pass
        return JsonResponse({})
    return JsonResponse({})

# Quản lý loại hàng


@decorators.login_required(login_url='/')
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


@decorators.login_required(login_url='/')
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

            return JsonResponse({"status": "success", "messages": 'Thêm thành công'})
        if is_edit != None:
            loai_hang = LoaiHang.objects.get(pk=id_loai_hang)
            loai_hang.ten_loai = ten_loai
            loai_hang.save()
            return JsonResponse({"status": "success", "messages": 'Sửa thành công'})
        if is_delete != None:
            loai_hang = LoaiHang.objects.get(pk=id_loai_hang).delete()
            return JsonResponse({"status": "success", "messages": 'Xóa thành công'})
    return JsonResponse({})


#  Nhà cung cấp
@decorators.login_required(login_url='/')
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
                return JsonResponse({"status": "success", "messages": 'Thêm thành công'})
            except:
                return JsonResponse({"status": "error", "messages": 'Lỗi'})

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

                return JsonResponse({"status": "success", "messages": 'Sửa thành công'})
            except:
                return JsonResponse({"status": "error", "messages": 'Lỗi'})
        if is_delete != None:
            try:
                ncc = NhaCungCap.objects.get(pk=id_ncc).delete()

                return JsonResponse({"status": "success", "messages": 'Xóa thành công'})
            except:
                return JsonResponse({"status": "error", "messages": 'Lỗi'})

    else:
        return JsonResponse({"status": "error", "messages": 'Lỗi'})
