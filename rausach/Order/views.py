import json
from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from django.contrib.auth import decorators

from Store.views import THEM_THANH_CONG, SUA_THANH_CONG, XOA_THANH_CONG, LOI
from Store.models import *

# Create your views here.


def base(request):
    loai_hang = LoaiHang.objects.all()
    return render(request, 'Order/layouts/base.html', {'loai_hang': loai_hang})


def index(request):
    san_pham = SanPham.objects.filter(is_active=1).order_by('-ngay_them')
    new_sp = SanPham.objects.filter(is_active=1).order_by('-khuyen_mai')[:6]
    paginator = Paginator(san_pham, 9)
    page = request.GET.get('page', 1)
    try:
        san_pham = paginator.page(page)
    except PageNotAnInteger:
        san_pham = paginator.page(1)
    except EmptyPage:
        san_pham = paginator.page(paginator.num_pages)

    loai_hang = LoaiHang.objects.all()
    data = {'san_pham': san_pham, 'loai_hang': loai_hang, 'new_sp': new_sp}
    return render(request, 'Order/index.html', data)


@decorators.login_required(login_url='/')
def loc_theo_loai_hang(request, loai_hang, id):
    san_pham = SanPham.objects.filter(is_active=1).filter(
        loai_hang=id).order_by('-ngay_them')
    paginator = Paginator(san_pham, 9)
    page = request.GET.get('page', 1)
    try:
        san_pham = paginator.page(page)
    except PageNotAnInteger:
        san_pham = paginator.page(1)
    except EmptyPage:
        san_pham = paginator.page(paginator.num_pages)

    loai_hang = LoaiHang.objects.all()
    data = {'san_pham': san_pham, 'loai_hang': loai_hang}
    return render(request, 'Order/index.html', data)


# @decorators.login_required(login_url='/')
def chi_tiet_hang(request, ten_hang, id):
    try:
        san_pham = SanPham.objects.get(pk=id)
    except ObjectDoesNotExist:
        loai_hang = LoaiHang.objects.all()
        return render(request, 'Order/product_detail.html',
                      {'loai_hang': loai_hang, 'not_found': '1'})
    loai_hang = LoaiHang.objects.all()
    anh_san_pham = HinhAnhSP.objects.filter(san_pham=san_pham.id)[:5]

    san_pham_lien_quan = SanPham.objects.filter(
        loai_hang=san_pham.loai_hang).filter(
            is_active=1).order_by('-ngay_them')[:5]
    data = {'loai_hang': loai_hang, 'san_pham': san_pham,
            'anh_san_pham': anh_san_pham,
            'san_pham_lien_quan': san_pham_lien_quan}

    if request.method == 'POST':
        try:
            hang_dat = HangDat()
            print(request.POST)
            hang_dat.nguoi_dung = request.user
            hang_dat.so_luong = request.POST.get('so_luong')
            print(request.POST.get('so_luong_con'))
            if int(request.POST.get('so_luong_con')) >= int(request.POST.get('so_luong')):
                hang_dat.trang_thai = TrangThaiHangHoa.objects.filter(
                    ma='ch').first()
            else:
                hang_dat.trang_thai = TrangThaiHangHoa.objects.filter(
                    ma='hh').first()
            hang_dat.hang_dat = SanPham.objects.get(
                pk=request.POST.get('hang_dat'))
            hang_dat.save()

            return JsonResponse(THEM_THANH_CONG)
        except:
            return JsonResponse(LOI)

    return render(request, 'Order/product_detail.html', data)


@decorators.login_required(login_url='/')
def thong_tin_ca_nhan(request):
    user = request.user
    if request.method == 'POST':
        if request.POST.get('password') == None:
            user.ho_ten = request.POST.get('ho_ten')
            user.gioi_tinh = request.POST.get('gioi_tinh')
            user.sdt = request.POST.get('sdt')
            user.dia_chi = request.POST.get('dia_chi')
            user.avatar = request.FILES.get('avatar')
            user.save()
        else:
            if request.POST.get('password') != request.POST.get('re-password'):
                messages.warning(request, 'Mật khẩu nhập lại không khớp')
            elif check_password(request.POST.get('old-password'),
                                user.password):
                user.set_password(request.POST.get('password'))
                user.save()
                messages.success(request, 'Đổi mật khẩu thành công')
                login(request, user)
            elif check_password(request.POST.get('old-password'),
                                user.password) == False:
                messages.warning(request, 'Mật khẩu cũ không đúng')
        return redirect('Order:thong_tin_ca_nhan')
    loai_hang = LoaiHang.objects.all()
    data = {'user': user, 'loai_hang': loai_hang}
    return render(request, 'Order/profile.html', data)


# Xử lý giỏ hàng
@decorators.login_required(login_url='/')
def gio_hang(request):
    user = request.user
    if request.method == 'POST':
        is_remove = request.POST.get('is_remove')
        id_hang_dat = request.POST.get('id_hang_dat')
        data = request.POST.get('data')

        if is_remove is not None:
            try:
                HangDat.objects.get(pk=id_hang_dat).delete()
                return JsonResponse(XOA_THANH_CONG)
            except:
                return JsonResponse(LOI)

        if data is not None:
            user = request.user
            data = json.loads(data)
            hoa_don = HoaDon()
            hoa_don.khach_hang = user
            hoa_don.ten_khach_hang = user.ho_ten
            hoa_don.trang_thai = TrangThaiHoaDon.objects.filter(
                ma='phrase1').first()
            hoa_don.save()
            id_hoa_don = hoa_don.id

            for item in data:
                chi_tiet_hoa_don = ChiTietHoaDon()
                hang_dat = HangDat.objects.get(pk=item['id_hang_dat'])
                hang_dat.check = 1
                hang_dat.save()
                chi_tiet_hoa_don.hoa_don = hoa_don
                sp = SanPham.objects.get(pk=item["id_hang"])
                chi_tiet_hoa_don.san_pham = sp
                chi_tiet_hoa_don.trang_thai = hang_dat.trang_thai
                print(hang_dat.trang_thai)
                chi_tiet_hoa_don.gia_ban = sp.gia_ban - \
                    int(sp.gia_ban * sp.khuyen_mai / 100)
                chi_tiet_hoa_don.so_luong_mua = item["so_luong"]
                chi_tiet_hoa_don.save()

            return JsonResponse(THEM_THANH_CONG)

    loai_hang = LoaiHang.objects.all()

    data = {'loai_hang': loai_hang}
    return render(request, 'Order/cart.html', data)


@decorators.login_required(login_url='/')
def data_gio_hang(request):
    user = request.user
    hang_dat = HangDat.objects.filter(nguoi_dung=user.id).filter(check=0)
    data = []
    i = 1
    for hd in hang_dat:
        obj = {}
        obj.update({'no': i})
        obj.update({'id': hd.id})
        obj.update({'so_luong': hd.so_luong})
        obj.update({'id_hang': hd.hang_dat.id})
        obj.update({'ten_hang': hd.hang_dat.ten_san_pham})
        if hd.trang_thai is not None:
            obj.update({'trang_thai': hd.trang_thai.mo_ta})
        else:
            obj.update({'trang_thai': ''})
        i += 1
        data.append(obj)

    return JsonResponse(data, safe=False)


@decorators.login_required(login_url='/')
def data_hoa_don(request):
    user = request.user
    hoa_don = HoaDon.objects.filter(khach_hang=user).order_by('-created_at')
    data = []
    i = 1
    for hd in hoa_don:
        obj = {}
        obj.update({'id': hd.id})
        obj.update({'ngay_lap': hd.created_at.strftime('%d-%m-%Y, %H:%M')})
        obj.update({'ma_trang_thai': hd.trang_thai.ma})
        obj.update({'trang_thai': hd.trang_thai.mo_ta})
        obj.update({'trang_thai_san+pham': hd.trang_thai.mo_ta})
        obj.update({'no': i})

        i += 1
        data.append(obj)

    return JsonResponse(data, safe=False)


@decorators.login_required(login_url='/')
def chi_tiet_hoa_don(request, id):
    if request.method == 'POST':
        HoaDon.objects.get(pk=id).delete()
        return redirect(reverse('Order:gio_hang'))
    hoa_don = HoaDon.objects.get(pk=id)
    ngay_lap = hoa_don.created_at.strftime('%d-%m-%Y, %H:%M')
    san_pham = ChiTietHoaDon.objects.filter(hoa_don=id)
    thanh_tien = 0
    for item in san_pham:
        thanh_tien += item.so_luong_mua * item.gia_ban
    data = {'hoa_don': hoa_don, 'san_pham': san_pham, 'ngay_lap': ngay_lap,
            'thanh_tien': thanh_tien}
    return render(request, 'Order/invoice_detail.html', data)


@decorators.login_required(login_url='/')
def data_chi_tiet_hoa_don(request, id):
    hoa_don = HoaDon.objects.get(pk=id)
    data_hoa_don = {}
    data_hoa_don.update({'ngay_lap': hoa_don.created_at.strftime('%d-%m-%Y,\
         %H:%M')})
    data_hoa_don.update({'trang_thai': hoa_don.trang_thai.mo_ta})
    ds_san_pham = ChiTietHoaDon.objects.filter(hoa_don=id)
    data = []
    for item in ds_san_pham:
        obj = {}
        obj.update({'id': item.id})
        obj.update({'so_luong_mua': item.so_luong_mua})
        obj.update({'gia_ban': item.gia_ban})
        print(item.trang_thai)
        if item.trang_thai.mo_ta is not None:
            obj.update({'trang_thai': item.trang_thai.mo_ta})
        else:
            obj.update({'trang_thai': 'item.trang_thai.mo_ta'})
        data.append(obj)

    response_data = {}
    response_data.update({'hoa_don': data_hoa_don})
    response_data.update({'san_pham': data})

    return JsonResponse(response_data, safe=False)


# Tìm kiếm
def search(request, ten):
    print(ten)
    san_pham = SanPham.objects.filter(
        ten_san_pham=ten).order_by('-ngay_them')
    paginator = Paginator(san_pham, 9)
    page = request.GET.get('page', 1)
    try:
        san_pham = paginator.page(page)
    except PageNotAnInteger:
        san_pham = paginator.page(1)
    except EmptyPage:
        san_pham = paginator.page(paginator.num_pages)

    loai_hang = LoaiHang.objects.all()
    data = {'san_pham': san_pham, 'loai_hang': loai_hang}
    return render(request, 'Order/search.html', data)


# Data tên sản phẩm
def data_ten_san_pham(request):
    san_pham = SanPham.objects.all()
    data = []
    for item in san_pham:
        data.append(item.ten_san_pham)
    return JsonResponse(data, safe=False)