from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galery/', views.galery, name='galery'),
    path('syarat-ketentuan/', views.syarat_ketentuan, name='syarat-ketentuan'),
]