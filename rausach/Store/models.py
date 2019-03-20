from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.


class MyUserManager(BaseUserManager):
    def create(self, username, password, ho_ten, sdt, role):
        user = self.model(
            username=username,
            ho_ten=ho_ten,
            sdt=sdt,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

# Bảng chứa thông tin nhân viên và người dùng


class MyUsers(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    ho_ten = models.TextField(blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.IntegerField(default=1)
    dia_chi = models.TextField(blank=True)
    huyen = models.TextField(max_length=255, blank=True)
    tinh = models.TextField(max_length=255, blank=True)
    ngay_sinh = models.DateField(default=timezone.now)
    luong = models.IntegerField(default=0)
    sdt = models.CharField(max_length=255)
    gioi_tinh = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.IntegerField()
    # role = 0 Superadmin
    # role = 1 Nhân viên trong cửa hàng
    # role = 2 Khách hàng
    USERNAME_FIELD = 'username'

    objects = MyUserManager()

    class Meta:
        db_table = 'my_users'

# Bảng loại hàng
class LoaiHang(models.Model):
    ten_loai = models.TextField()

    class Meta:
        db_table = 'loai_hang'
# Bảng sản phẩm


class SanPham(models.Model):
    ten_san_pham = models.TextField()
    ngay_them = models.DateField(auto_now_add=True)
    # Giá vốn
    gia_von = models.IntegerField(default=0)
    gia_ban = models.IntegerField(default=0)
    # Số lượng
    so_luong = models.IntegerField(default=0)
    # Tồn kho
    ton_kho = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    loai_hang = models.ForeignKey('LoaiHang', models.SET_NULL, null=True)
    mo_ta = models.TextField(blank=True)
    nha_cung_cap = models.ForeignKey('NhaCungCap', models.SET_NULL, null=True)

    class Meta:
        db_table = 'san_pham'

# Bảng chứa hình ảnh của các sản phẩm


class HinhAnhSP(models.Model):
    san_pham = models.ForeignKey('SanPham', models.CASCADE)
    hinh_anh = models.FileField(upload_to='product/')
    duong_dan = models.FilePathField()

    class Meta:
        db_table = 'hinh_anh_san_pham'

# Nhà cung cấp


class NhaCungCap(models.Model):
    ten = models.TextField()
    sdt = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    dia_chi = models.TextField(blank=True)
    huyen = models.CharField(max_length=255, blank=True)
    tinh = models.CharField(max_length=255, blank=True)
    is_active = models.IntegerField(default=1)
    mo_ta = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'nha_cung_cap'

# Hóa đơn


class HoaDon(models.Model):
    khach_hang = models.ForeignKey(
        'MyUsers', models.SET_NULL, related_name='khach_hang', null=True)
    ngay_lap = models.DateTimeField(default=timezone.now)
    created_at = models.DateField(auto_now_add=True)
    ghi_chu = models.TextField()
    nguoiTao = models.ForeignKey(
        'MyUsers', models.SET_NULL, related_name='nguoi_tao_hoa_don', null=True)
    is_paid = models.IntegerField(default=0)

    class Meta:
        db_table = 'hoa_don'

# Chi tiết hóa đơn


class ChiTietHoaDon(models.Model):
    san_pham = models.ForeignKey(
        'SanPham', models.SET_NULL, related_name='san_pham_hoa_don', null=True)
    hoa_don = models.ForeignKey(
        'HoaDon', models.SET_NULL, related_name='hoa_don', null=True)
    # Số lượng mua
    so_luong_mua = models.IntegerField(default=0)

    class Meta:
        db_table = 'chi_tiet_hoa_don'

# Phiếu trả hàng


class PhieuTra(models.Model):
    thoi_gian_tra = models.DateTimeField(auto_now_add=True)
    ghi_chu = models.TextField(blank=True)
    khach_hang_tra = models.ForeignKey(
        'MyUsers', models.SET_NULL, related_name='khach_hang_tra', null=True)
    nguoi_ban = models.ForeignKey(
        'MyUsers', models.SET_NULL, related_name='nguoi_ban', null=True)
    nguoi_tao = models.ForeignKey(
        'MyUsers', models.SET_NULL, related_name='nguoi_tao_phieu_tra', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'phieu_tra_hang'

# Chi tiết phiếu trả


class ChiTietPhieuTra(models.Model):
    # Giá nhập lại
    gia_nhap_lai = models.IntegerField(default=0)
    phieu_tra = models.ForeignKey(
        'PhieuTra', models.CASCADE, related_name='phieu_tra')
    san_pham = models.ForeignKey(
        'SanPham', models.SET_NULL, related_name='san_pham_phieu_tra', null=True)

    class Meta:
        db_table = 'chi_tiet_phieu_tra'

# Phiếu nhập


class PhieuNhap(models.Model):
    thoi_gian_nhap = models.DateTimeField(auto_now_add=True)
    ghi_chu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    nguoi_tao = models.ForeignKey('MyUsers', models.SET_NULL, null=True)
    nha_cung_cap = models.ForeignKey('NhaCungCap', models.SET_NULL, null=True)

    class Meta:
        db_table = 'phieu_nhap'

# Chi tiết phiếu nhập


class ChiTietPhieuNhap(models.Model):
    san_pham = models.ForeignKey('SanPham', models.CASCADE)
    so_luong = models.IntegerField(default=0)
    don_gia_nhap = models.IntegerField(default=0)
    phieu_nhap = models.ForeignKey('PhieuNhap', models.SET_NULL, null=True)

    class Meta:
        db_table = 'chi_tiet_phieu_nhap'

# Phiếu trả hàng nhập


class PhieuTraHangNhap(models.Model):
    thoi_gian_tao = models.DateTimeField(default=timezone.now)
    ghi_chu = models.TextField()
    nguoi_tao = models.ForeignKey('MyUsers', models.SET_NULL, null=True)
    nha_cung_cap = models.ForeignKey('NhaCungCap', models.SET_NULL, null=True)

    class Meta:
        db_table = 'phieu_tra_hang_nhap'

# Chi tiết phiếu trả hàng nhập


class ChiTietPhieuTraHangNhap(models.Model):
    phieu_tra_hang_nhap = models.ForeignKey('PhieuTraHangNhap', models.CASCADE)
    so_luong = models.IntegerField(default=0)
    gia_tra_lai = models.IntegerField(default=0)
    san_pham = models.ForeignKey('SanPham', models.SET_NULL, null=True)

    class Meta:
        db_table = 'chi_tiet_phieu_tra_hang_nhap'

# Phiếu xuất hủy


class PhieuXuatHuy(models.Model):
    thoi_gian_tao = models.DateTimeField(timezone.now)
    ghi_chu = models.TextField()
    nguoi_tao = models.ForeignKey('MyUsers', models.SET_NULL, null=True)

    class Meta:
        db_table = 'phieu_xuat_huy'

# Chi tiết phiếu xuất hủy


class ChiTietPhieuXuatHuy(models.Model):
    phieu_xuat_huy = models.ForeignKey('PhieuXuatHuy', models.CASCADE)
    san_pham = models.ForeignKey('SanPham', models.SET_NULL, null=True)
    so_luong = models.IntegerField(default=0)

    class Meta:
        db_table = 'chi_tiet_phieu_xuat_huy'
