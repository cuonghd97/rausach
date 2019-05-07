from django.urls import path, include

from Order import views

app_name = "Order"

urlpatterns = [
    path('base/', views.base),
    path('', views.index, name='index'),
    path('quanly', include([
        path('-gio-hang/', views.gio_hang, name='gio_hang')
    ])),
    path('data', include([
        path('-gio-hang/', views.data_gio_hang),
        path('-hoa-don/', views.data_hoa_don),
        path('-chi-tiet-hoa-don/<int:id>/', views.data_chi_tiet_hoa_don),
        path('-ten-san-pham/', views.data_ten_san_pham)
    ])),
    # path('post', include([
    # ])),
    path('filter/', include([
        path(
            '<str:loai_hang>_<int:id>/',
            views.loc_theo_loai_hang,
            name='loc_theo_loai_hang'),
    ])),
    path('detail/', include([
        path(
            'hang/<str:ten_hang>_<int:id>/',
            views.chi_tiet_hang,
            name='chi_tiet_hang'),
        path(
            'nguoi-dung/',
            views.thong_tin_ca_nhan,
            name='thong_tin_ca_nhan'),
        path(
            'invoice/<int:id>/',
            views.chi_tiet_hoa_don,
            name='chi_tiet_hoa_don')
    ])),
    path('search/<str:ten>/', views.search, name='search')
]
