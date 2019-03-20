from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from Store.models import MyUsers
# Create your views here.

def user_login(request):
    user = request.user
    if user.is_authenticated:
        if user.role == 0:
            return redirect(reverse('Store:base'))
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                user = MyUsers.objects.get(username=username)
            except ObjectDoesNotExist:
                return JsonResponse({"status": "error", "messages": 'Tên đăng nhập hoặc mật khẩu không đúng'})
            else:
                if check_password(password, user.password):
                    login(request, user)
                    if user.role == 0:
                        return JsonResponse({"status": "success", "messages": reverse('Store:base')})
                    if user.role == 1:
                        return JsonResponse({"status": "success", "messages": 'Nhân viên'})
                    elif user.role == 2:
                        return JsonResponse({"status": "success", "messages": 'Người dùng'})
                else:
                    return JsonResponse({"status": "error", "messages": 'Tên đăng nhập hoặc mật khẩu không đúng'})
    return render(request, 'General/login.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('General:login'))