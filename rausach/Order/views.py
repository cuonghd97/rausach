import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth import login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from Store.views import THEM_THANH_CONG, SUA_THANH_CONG, XOA_THANH_CONG, LOI

from Store.models import *

# Create your views here.

def base(request):
    loai_hang = LoaiHang.objects.all()
    return render(request, 'Order/layouts/base.html', {'loai_hang': loai_hang})

def index(request):
    san_pham = SanPham.objects.filter(is_active=1).order_by('-ngay_them')
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

def loc_theo_loai_hang(request,loai_hang, id):
    san_pham = SanPham.objects.filter(is_active=1).filter(loai_hang=id).order_by('-ngay_them')
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

def chi_tiet_hang(request, ten_hang, id):
    try:
        san_pham = SanPham.objects.get(pk=id)
    except ObjectDoesNotExist:
        loai_hang = LoaiHang.objects.all()
        return render(request, 'Order/product_detail.html', {'loai_hang': loai_hang, 'not_found': '1'})
    loai_hang = LoaiHang.objects.all()
    anh_san_pham = HinhAnhSP.objects.filter(san_pham=san_pham.id)[:5]

    san_pham_lien_quan = SanPham.objects.filter(loai_hang=san_pham.loai_hang).filter(is_active=1).order_by('-ngay_them')[:5]
    data = {'loai_hang': loai_hang, 'san_pham': san_pham, 'anh_san_pham': anh_san_pham, 'san_pham_lien_quan': san_pham_lien_quan}

    if request.method == 'POST':
        try:
            hang_dat = HangDat()
            hang_dat.nguoi_dung = request.user
            hang_dat.so_luong = request.POST.get('so_luong')
            hang_dat.hang_dat = SanPham.objects.get(pk=request.POST.get('hang_dat'))
            hang_dat.save()

            return JsonResponse(THEM_THANH_CONG)
        except:
            return JsonResponse(LOI)
    
    return render(request, 'Order/product_detail.html', data)

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
            elif check_password(request.POST.get('old-password'), user.password):
                user.set_password(request.POST.get('password'))
                user.save()
                messages.success(request, 'Đổi mật khẩu thành công')
                login(request, user)
            elif check_password(request.POST.get('old-password'), user.password) == False: 
                messages.warning(request, 'Mật khẩu cũ không đúng')
        return redirect('Order:thong_tin_ca_nhan')
    loai_hang = LoaiHang.objects.all()
    data = {'user': user, 'loai_hang': loai_hang}
    return render(request, 'Order/profile.html', data)

# Xử lý giỏ hàng
def gio_hang(request):
    user = request.user
    if request.method == 'POST':
        is_remove = request.POST.get('is_remove')
        id_hang_dat = request.POST.get('id_hang_dat')
        data = request.POST.get('data')

        if is_remove != None:
            try:
                HangDat.objects.get(pk=id_hang_dat).delete()
                return JsonResponse(XOA_THANH_CONG)
            except:
                return JsonResponse(LOI)
        
        if data != None:
            user = request.user
            data = json.loads(data)
            print(data[0])
            hoa_don = HoaDon()
            hoa_don.khach_hang = user
            hoa_don.save()
            id_hoa_don = hoa_don.id

            for item in data:
                chi_tiet_hoa_don = ChiTietHoaDon()
                chi_tiet_hoa_don.hoa_don = hoa_don
                chi_tiet_hoa_don.san_pham = SanPham.objects.get(pk=item["id_hang"])
                chi_tiet_hoa_don.so_luong_mua = item["so_luong"]
                chi_tiet_hoa_don.save()

            return JsonResponse(THEM_THANH_CONG)
    
    loai_hang = LoaiHang.objects.all()
    
    data = {'loai_hang': loai_hang}
    return render(request, 'Order/cart.html', data)

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

        i+=1
        data.append(obj)

    return JsonResponse(data, safe=False)