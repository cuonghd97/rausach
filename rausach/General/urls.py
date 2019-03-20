from django.urls import path

from General import views

app_name='General'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout')
]