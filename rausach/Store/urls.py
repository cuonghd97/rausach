from django.urls import path, include

from Store import views

app_name='Store'

urlpatterns = [
	path('base/', views.base, name='base'),
	path('quanly', include([
		path('-san-pham/', views.san_pham, name='quan_ly_san_pham'),
		path('-loai-hang/', views.loai_hang, name='quan_ly_loai_hang'),
		path('-nha-cung-cap/', views.nha_cung_cap, name='quan_ly_nha_cung_cap'),
	])),
	path('data', include([
		path('-san-pham/', views.data_san_pham),
		path('-loai-hang/', views.data_loai_hang),
		path('-nha-cung-cap/', views.data_nha_cung_cap),
		path('-tinh/', views.data_tinh),
		path('-huyen/', views.data_huyen)
	])),
	path('post', include([
		path('-loai-hang/', views.post_loai_hang),
		path('-nha-cung-cap/', views.post_nha_cung_cap),
	]))
]