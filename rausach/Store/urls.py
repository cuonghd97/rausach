from django.urls import path

from Store import views

app_name='Store'

urlpatterns = [
	path('base/', views.base, name='base')
]