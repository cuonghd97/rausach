from django.db import models
from django.utils import timezone
import os
from uuid import uuid4
import datetime
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUsers(AbstractUser):
    tenNguoiDung = models.TextField(max_length=200, null=True)
    luong = models.IntegerField(default=0)
    dienThoai = models.CharField(max_length=200, null=True)
    diaChi = models.TextField(max_length=200, null=True)
    phuongXa = models.TextField(max_length=200, null=True)
    huyen = models.TextField(max_length=200, null=True)
    tinh = models.TextField(max_length=200, null=True)
    role = models.IntegerField(default=1)
    # 1 Nhân viên
    # 2 Khách hàng
    # 0 Superuser
    email = models.TextField(max_length=200, null=True)
    ngaySinh = models.DateField(default=timezone.now)
    ngayTao = models.DateField(default=timezone.now)
    gioiTinh = models.TextField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "myusers"

class Anh(models.Model):
    def path_and_rename(instance, filename):
        upload_to = 'ImageProducts'
        ext = filename.split('.')[-1]
        
        filename = '{}.{}'.format(uuid4().hex, ext)

        print(filename)

        return os.path.join(upload_to, filename)

    hangHoa = models.ForeignKey('HangHoa', models.CASCADE)
    path = models.FileField(upload_to=path_and_rename)
    tenAnh = models.CharField(max_length=200, blank=True)
    is_main = models.IntegerField(default=0)

# class KhachHang(models.Model):
#     tenKhachHang = models.TextField(max_length=200, null=True)
#     email = models.TextField(max_length=200, null=True)
#     dienThoai = models.CharField(max_length=200, null=True)
#     diaChi = models.TextField(max_length=200, null=True)
#     gioiTinh = models.TextField(max_length=200, null=True)
#     ngaySinh = models.DateField(datetime.date.today)
#     ngayTao = models.DateTimeField(timezone.now)
#     diaChi = models.TextField(max_length=200, null=True)
#     phuongXa = models.TextField(max_length=200, null=True)
#     huyen = models.TextField(max_length=200, null=True)
#     tinh = models.TextField(max_length=200, null=True)

#     class Meta:
#         managed = True
#         db_table = "khach_hang"


class NhaCungCap(models.Model):
    maNhaCungCap = models.CharField(max_length=200, null=True)
    tenNhaCungCap = models.TextField(max_length=200, null=True)
    dienThoai = models.CharField(max_length=200, null=True)
    email = models.TextField(max_length=200, null=True)
    diaChi = models.TextField(max_length=200, null=True)
    phuongXa = models.TextField(max_length=200, null=True)
    huyen = models.TextField(max_length=200, null=True)
    tinh = models.TextField(max_length=200, null=True)
    trangThai = models.CharField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "nha_cung_cap"


class HangHoa(models.Model):
    maHang = models.CharField(max_length=200, null=True)
    tenHang = models.TextField(max_length=200, null=True)
    soLuong = models.IntegerField(default=0)
    ngayNhap = models.DateTimeField(default=timezone.now)
    giaBan = models.IntegerField(default=0)
    giaVon = models.IntegerField(default=0)
    tonKho = models.IntegerField(default=0)
    trangThai = models.CharField(max_length=200, null=True)
    loaiHang = models.TextField(max_length=200, null=True)
    soLuong = models.IntegerField(default=0)
    moTa = models.TextField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "hang_hoa"


class HoaDon(models.Model):
    maHoaDon = models.CharField(max_length=200, null=True)
    thoiGianTao = models.DateTimeField(timezone.now)
    khachHang = models.ForeignKey(MyUsers, models.SET_NULL, related_name='khachHangHoaDon', null=True)
    nguoiTao = models.ForeignKey(MyUsers, models.SET_NULL, related_name='nguoiTaoHoaDon', null=True)
    ghiChu = models.TextField(max_length=200, null=True)
    trangThai = models.CharField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "hoa_don"


class ChiTietHoaDon(models.Model):
    hoaDon = models.ForeignKey(HoaDon, models.CASCADE, null=True)
    hangHoa = models.ForeignKey(HangHoa, models.SET_NULL, null=True)
    soLuongMua = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = "chi_tiet_hoa_don"


class PhieuTraHang(models.Model):
    maPhieu = models.CharField(max_length=200, null=True)
    nguoiBan = models.ForeignKey(
        MyUsers, models.SET_NULL, related_name="nguoiBan", null=True)
    thoiGianTra = models.DateTimeField(timezone.now)
    khachHangTra = models.ForeignKey(MyUsers, models.SET_NULL, null=True)
    nguoiTao = models.ForeignKey(
        MyUsers, models.SET_NULL, related_name="nguoiTao", null=True)
    ghiChu = models.TextField(max_length=200, null=True)
    trangThai = models.CharField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "phieu_tra_hang"


class ChiTietPhieuTra(models.Model):
    phieuTra = models.ForeignKey(PhieuTraHang, models.CASCADE, null=True)
    maHang = models.ForeignKey(HangHoa, models.SET_NULL, null=True)
    soLuongTra = models.IntegerField(default=0)
    giaNhapLai = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = "chi_tiet_phieu_tra"


class PhieuNhap(models.Model):
    maPhieu = models.CharField(max_length=200, null=True)
    thoiGianNhap = models.DateTimeField(timezone.now)
    nhaCungCap = models.ForeignKey(NhaCungCap, models.SET_NULL, null=True)
    ghiChu = models.TextField(max_length=200, null=True)
    trangThai = models.CharField(max_length=200, null=True)
    thoiGianTao = models.DateTimeField(timezone.now)
    nguoiTao = models.ForeignKey(MyUsers, models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = "phieu_nhap"


class ChiTietPhieuNhap(models.Model):
    phieuNhap = models.ForeignKey(PhieuNhap, models.SET_NULL, null=True)
    tenHang = models.TextField(max_length=200, null=True)
    soLuong = models.IntegerField(default=0)
    donGiaNhap = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = "chi_tiet_phieu_nhap"


class PhieuTraHangNhap(models.Model):
    maPhieu = models.CharField(max_length=200, null=True)
    thoiGianTao = models.DateTimeField(timezone.now)
    nhaCungCapTra = models.ForeignKey(NhaCungCap, models.SET_NULL, null=True)
    ghiChu = models.TextField(max_length=200, null=True)
    nguoiTao = models.ForeignKey(MyUsers, models.SET_NULL, null=True)
    ghiChu = models.TextField(max_length=200, null=True)
    trangThai = models.CharField(max_length=200, null=True)

    class Meta:
        managed = True
        db_table = "phieu_tra_hang_nhap"


class ChiTietTraHangNhap(models.Model):
    phieuTraHangNhap = models.ForeignKey(
        PhieuTraHangNhap, models.SET_NULL, null=True)
    hangHoa = models.ForeignKey(HangHoa, models.SET_NULL, null=True)
    soLuong = models.IntegerField(default=0)
    giaTraLai = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = "chi_tiet_tra_hang_nhap"


class PhieuXuatHuy(models.Model):
    maXuatHuy = models.CharField(max_length=200, null=True)
    thoiGianTao = models.DateTimeField(timezone.now)
    thoiGianXuatHuy = models.DateTimeField(timezone.now)
    ghiChu = models.TextField(max_length=200, null=True)
    trangThai = models.TextField(max_length=200, null=True)
    nguoiTao = models.ForeignKey(MyUsers, models.SET_NULL, null=True)

    class Meta:
        managed = True
        db_table = "phieu_xuat_huy"


class ChiTietXuatHuy(models.Model):
    xuatHuy = models.ForeignKey(PhieuXuatHuy, models.SET_NULL, null=True)
    hangHoa = models.ForeignKey(HangHoa, models.SET_NULL, null=True)
    soLuongHuy = models.IntegerField(default=0)

    class Meta:
        managed = True
        db_table = "chi_tiet_xuat_huy"
