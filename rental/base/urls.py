from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galery/', views.galery, name='galery'),
    path('syarat-ketentuan/', views.syarat_ketentuan, name='syarat-ketentuan'),
    path('adm/', views.adm, name='adm'),
    path('kontak/', views.contact, name='kontak'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_page, name='register'),
]