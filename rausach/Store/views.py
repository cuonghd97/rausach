import json

from django.shortcuts import render
from django.contrib.auth import decorators
from django.http import HttpResponse, JsonResponse

from General.decorators import is_admin
from Store import models

# Create your views here.


def base(request):
    return render(request, 'Store/layouts/base.html')

# Quản lý sản phẩm trong cửa hàng
@decorators.login_required(login_url='/')
@is_admin
def san_pham(request):
    return render(request, 'Store/categories/products.html')
# Data sản phẩm


def data_san_pham(request):
    pass

# Quản lý loại hàng

@decorators.login_required(login_url='/')
@is_admin
def loai_hang(request):
    return render(request, 'Store/categories/categories.html')

# Data loại hàng


def data_loai_hang(request):
    loai_hang = models.LoaiHang.objects.all()
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
			loai_hang = models.LoaiHang()
			loai_hang.ten_loai = ten_loai
			loai_hang.save()
		
			return JsonResponse({"status": "success", "messages": 'Thêm thành công'})
		if is_edit != None:
			loai_hang = models.LoaiHang.objects.get(pk=id_loai_hang)
			loai_hang.ten_loai = ten_loai
			loai_hang.save()
			return JsonResponse({"status": "success", "messages": 'Sửa thành công'})
		if is_delete != None:
			loai_hang = models.LoaiHang.objects.get(pk=id_loai_hang).delete()
			return JsonResponse({"status": "success", "messages": 'Xóa thành công'})
	return JsonResponse({})
