from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate, login, decorators, logout, get_user
from .models import NhanVien
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def Base(request):
  if not request.user.is_authenticated:
    messages.warning(request, "Sai ten dang nhap hoac mat khau")
    return render(request, 'login.html')
  return render(request, 'base.html')

def Direct(request):
  return redirect("ManageStore:login")

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
    return redirect('ManageStore:base')

# Logout
def UserLogout(request):
  logout(request)
  return redirect('ManageStore:login')