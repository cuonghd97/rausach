from django.urls import path

from Store import views

app_name='Store'

urlpatterns = [
	path('', views.base)
]