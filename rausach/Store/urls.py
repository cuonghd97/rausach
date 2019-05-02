from django.urls import path, include

from Store import views

app_name = 'Store'

urlpatterns = [
    path('base/', views.base, name='base'),
    path('quanly', include([
        path('-san-pham/', views.san_pham, name='quan_ly_san_pham'),
        path('-loai-hang/', views.loai_hang, name='quan_ly_loai_hang'),
        path('-nha-cung-cap/', views.nha_cung_cap, name='quan_ly_nha_cung_cap'),
        path('-nhan-vien/', views.nhan_vien, name='quan_ly_nhan_vien'),
        path('-nguoi-dung/', views.nguoi_dung, name='quan_ly_nguoi_dung'),
        path('-hoa-don/', views.hoa_don, name='quan_ly_hoa_don'),
        path('-ban-hang/', views.ban_hang, name='ban_hang')
    ])),
    path('data', include([
        path('-san-pham/', views.data_san_pham),
        path('-loai-hang/', views.data_loai_hang),
        path('-nha-cung-cap/', views.data_nha_cung_cap),
        path('-tinh/', views.data_tinh),
        path('-huyen/', views.data_huyen),
        path('-anh-san-pham/<int:id>', views.data_anh_sp),
        path('-nhan-vien/', views.data_nhan_vien),
        path('-nguoi-dung/', views.data_nguoi_dung),
        path('-hoa-don/', views.data_hoa_don),
        path('-chi-tiet-hoa-don/<int:id>', views.chi_tiet_hoa_don),
        path('-trang-thai/', views.data_trang_thai)
    ])),
    path('post', include([
        path('-loai-hang/', views.post_loai_hang),
        path('-nha-cung-cap/', views.post_nha_cung_cap),
        path('-san-pham/', views.post_san_pham),
        path('-nhan-vien/', views.post_nhan_vien),
        path('-nguoi-dung/', views.post_nguoi_dung)
    ]))
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
