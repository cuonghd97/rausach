from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils import timezone

# Create your models here.


class MyUsersManager(BaseUserManager):
    def create(self, username, password, ho_ten, sdt, role, is_active=1):
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
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    ho_ten = models.TextField(blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.IntegerField(default=1)
    is_active = models.IntegerField(default=1)
    dia_chi = models.TextField(blank=True)
    huyen = models.TextField(max_length=255, blank=True)
    tinh = models.TextField(max_length=255, blank=True)
    ngay_sinh = models.DateField(default=timezone.now)
    luong = models.IntegerField(default=0)
    sdt = models.CharField(max_length=255)
    gioi_tinh = models.CharField(max_length=10, blank=True)
    # gioi_tinh = nam: Nam
    # gioi_tinh = nu: Nữ
    # gioi_tinh = oth: Khác
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.IntegerField()
    # role = 0 Superadmin
    # role = 1 Nhân viên bán hàng
    # role = 2 Thủ kho
    # role = 3 Khách hàng
    is_active = models.BooleanField(default=False)
    avatar = models.FileField(upload_to='users/')

    USERNAME_FIELD = 'username'

    objects = MyUsersManager()

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
    khuyen_mai = models.IntegerField(default=0)
    # Số lượng
    so_luong = models.IntegerField(default=0)
    # Tồn kho
    ton_kho = models.IntegerField(default=0)
    is_active = models.IntegerField(default=1)
    loai_hang = models.ForeignKey('LoaiHang', models.SET_NULL, null=True)
    mo_ta = models.TextField(blank=True)
    nha_cung_cap = models.ForeignKey('NhaCungCap', models.SET_NULL, null=True)
    avt = models.FileField(upload_to='product/avatar/')
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'san_pham'

# Bảng chứa hình ảnh của các sản phẩm


class HinhAnhSP(models.Model):
    san_pham = models.ForeignKey('SanPham', models.CASCADE)
    hinh_anh = models.FileField(upload_to='product/')
    # duong_dan = models.FilePathField()

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
    ten_khach_hang = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    ghi_chu = models.TextField(null=True)
    sdt = models.CharField(max_length=200)
    dia_chi = models.TextField()
    nguoiTao = models.ForeignKey(
        'MyUsers', models.SET_NULL, related_name='nguoi_tao_hoa_don',
        null=True)
    trang_thai = models.ForeignKey('TrangThaiHoaDon', models.SET_NULL, null=True)

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
    gia_ban = models.IntegerField(default=0)

    class Meta:
        db_table = 'chi_tiet_hoa_don'

# Phiếu trả hàng


# class PhieuTra(models.Model):
#     thoi_gian_tra = models.DateTimeField(auto_now_add=True)
#     ghi_chu = models.TextField(blank=True)
#     khach_hang_tra = models.ForeignKey(
#         'MyUsers', models.SET_NULL, related_name='khach_hang_tra', null=True)
#     nguoi_ban = models.ForeignKey(
#         'MyUsers', models.SET_NULL, related_name='nguoi_ban', null=True)
#     nguoi_tao = models.ForeignKey(
#         'MyUsers', models.SET_NULL, related_name='nguoi_tao_phieu_tra',
#         null=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'phieu_tra_hang'

# # Chi tiết phiếu trả


# class ChiTietPhieuTra(models.Model):
#     # Giá nhập lại
#     gia_nhap_lai = models.IntegerField(default=0)
#     phieu_tra = models.ForeignKey(
#         'PhieuTra', models.CASCADE, related_name='phieu_tra')
#     san_pham = models.ForeignKey(
#         'SanPham', models.SET_NULL, related_name='san_pham_phieu_tra',
#         null=True)

#     class Meta:
#         db_table = 'chi_tiet_phieu_tra'

# # Phiếu nhập


# class PhieuNhap(models.Model):
#     thoi_gian_nhap = models.DateTimeField(auto_now_add=True)
#     ghi_chu = models.TextField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     nguoi_tao = models.ForeignKey('MyUsers', models.SET_NULL, null=True)
#     nha_cung_cap = models.ForeignKey('NhaCungCap', models.SET_NULL,
#        null=True)

#     class Meta:
#         db_table = 'phieu_nhap'

# # Chi tiết phiếu nhập


# class ChiTietPhieuNhap(models.Model):
#     san_pham = models.ForeignKey('SanPham', models.CASCADE)
#     so_luong = models.IntegerField(default=0)
#     don_gia_nhap = models.IntegerField(default=0)
#     phieu_nhap = models.ForeignKey('PhieuNhap', models.SET_NULL, null=True)

#     class Meta:
#         db_table = 'chi_tiet_phieu_nhap'

# # Phiếu trả hàng nhập


# class PhieuTraHangNhap(models.Model):
#     thoi_gian_tao = models.DateTimeField(default=timezone.now)
#     ghi_chu = models.TextField(null=True)
#     nguoi_tao = models.ForeignKey('MyUsers', models.SET_NULL, null=True)
#     nha_cung_cap = models.ForeignKey('NhaCungCap', models.SET_NULL,
#         null=True)

#     class Meta:
#         db_table = 'phieu_tra_hang_nhap'

# # Chi tiết phiếu trả hàng nhập


# class ChiTietPhieuTraHangNhap(models.Model):
#     phieu_tra_hang_nhap = models.ForeignKey('PhieuTraHangNhap',
#         models.CASCADE)
#     so_luong = models.IntegerField(default=0)
#     gia_tra_lai = models.IntegerField(default=0)
#     san_pham = models.ForeignKey('SanPham', models.SET_NULL, null=True)

#     class Meta:
#         db_table = 'chi_tiet_phieu_tra_hang_nhap'

# # Phiếu xuất hủy


# class PhieuXuatHuy(models.Model):
#     thoi_gian_tao = models.DateTimeField(auto_now_add=True)
#     ghi_chu = models.TextField(null=True)
#     nguoi_tao = models.ForeignKey('MyUsers', models.SET_NULL, null=True)

#     class Meta:
#         db_table = 'phieu_xuat_huy'

# # Chi tiết phiếu xuất hủy


# class ChiTietPhieuXuatHuy(models.Model):
#     phieu_xuat_huy = models.ForeignKey('PhieuXuatHuy', models.CASCADE)
#     san_pham = models.ForeignKey('SanPham', models.SET_NULL, null=True)
#     so_luong = models.IntegerField(default=0)

#     class Meta:
#         db_table = 'chi_tiet_phieu_xuat_huy'

# class Log(models.Model):
#     BAN_DON_HANG = "bán đơn hàng"
#     NHAP_HANG = "nhập hàng"
#     TRA_HANG = "trả hàng"
#     TRA_HANG_NHAP = "trả hàng nhập"
#     XUAT_HUY = "xuất hủy"
#     created_at = models.DateTimeField(auto_now_add=True)
#     nguoi_tao = models.ForeignKey(
#         "MyUsers", models.SET_NULL, related_name='nguoi_tao', null=True)
#     hanh_dong = models.TextField()
#     hoa_don = models.ForeignKey(
#         "HoaDon", models.SET_NULL, related_name='log_hoa_don', null=True)
#     # phieu_tra = models.ForeignKey("PhieuTra", models.SET_NULL,
#     #     related_name='log_phieu_tra', null=True)
#     # phieu_nhap = models.ForeignKey("PhieuNhap", models.SET_NULL,
#     #     related_name='log_phieu_nhap', null=True)
#     # phieu_tra_hang_nhap = models.ForeignKey("PhieuTraHangNhap",
#     #     models.SET_NULL, related_name='log_phieu_tra_hang_nhap', null=True)
#     # phieu_xuat_huy = models.ForeignKey("PhieuXuatHuy", models.SET_NULL,
#     #     related_name='log_phieu_xuat_huy', null=True)

#     class Meta:
#         db_table = 'log'


class SoQuy(models.Model):
    tong_thu = models.IntegerField(default=0)
    tong_chi = models.IntegerField(default=0)

    class Meta:
        db_table = 'so_quy'


class HangDat(models.Model):
    nguoi_dung = models.ForeignKey('MyUsers', models.CASCADE)
    hang_dat = models.ForeignKey('SanPham', models.CASCADE)
    so_luong = models.IntegerField(default=0)
    check = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hang_dat'


class TrangThaiHoaDon(models.Model):
    '''
    Các trạng thái của hóa đơn:
        Mới: Đơn hàng khách chưa qua xử lý.
        Chờ đi nhận: Chờ hàng vận chuyển tiếp nhận thông tin hàng.
        Đã nhận hàng: Đơn hàng đã được hãng vận chuyển tiếp nhận.
        Đang chuyển: Đơn hàng đang được chuyển đi cho khách hàng.
        Thành công: Đơn hàng đã được giao thành công cho khách hàng.
        Thất bại: Đơn hàng chưa được chuyển cho khách hàng.
        Hết hàng: Sản phẩm khách đặt đã hết hàng.
    '''
    ma = models.CharField(max_length=200)
    mo_ta = models.TextField()

    class Meta:
        db_table = 'trang_thai'
