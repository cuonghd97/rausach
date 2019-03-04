from django.urls import path
from Shop import views

app_name='Shop'

urlpatterns = [
    path('', views.index)
]