from django.urls import path
from . import views

app_name = "ManageStore"

urlpatterns = [
  path('', views.Direct),
  path('login/', views.LoginClass.as_view(), name="login"),
  path('base/', views.Base, name='base'),
  path('logout/', views.UserLogout, name="logout")
]