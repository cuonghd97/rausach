from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from Store.models import MyUsers
# Create your views here.

def user_login(request):
    user = request.user
    if user.is_authenticated:
        if user.role == 0:
            return JsonResponse({"status": "success", "messages": reverse('Store:base')})
        if user.role == 2:
            return JsonResponse({"status": "success", "messages": 'Bán hàng'})
        if user.role == 3:
            return JsonResponse({"status": "success", "messages": reverse('Order:index')})
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
                    if user.role == 2:
                        return JsonResponse({"status": "success", "messages": 'Bán hàng'})
                    if user.role == 3:
                        return JsonResponse({"status": "success", "messages": reverse('Order:index')})
                else:
                    return JsonResponse({"status": "False", "messages": 'Tên đăng nhập hoặc mật khẩu không đúng'})
    return render(request, 'General/login.html')

def user_register(request):
    if request.method == 'POST':
        if request.POST.get('password') != request.POST.get('re-password'):
            messages.success(request, 'Mật khẩu nhập lại không khớp')
            return redirect('General:register')
        elif MyUsers.objects.filter(username=request.POST.get('username')).first() != None:
            messages.success(request, 'Trùng tên đăng nhập')
            return redirect('General:register')
        elif MyUsers.objects.filter(email=request.POST.get('email')).first() != None:
            messages.success(request, 'Email này đã được đăng ký')
            return redirect('General:register')
        else:
            try:
                user = MyUsers()
                user.ho_ten = request.POST.get('ho_ten')
                user.username = request.POST.get('username')
                user.set_password(request.POST.get('password'))
                user.email = request.POST.get('email')
                user.is_active = 1
                user.role = 3
                user.save()
                login(request, user)
                return redirect('Order:index')
            except:
                messages.success(request, 'Lỗi')
                return redirect('General:register')
    return render(request, 'General/register.html')

def user_logout(request):
    logout(request)
    return redirect(reverse('Order:index'))