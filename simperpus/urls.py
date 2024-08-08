"""
URL configuration for simperpus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perpus_app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', beranda, name='beranda'),
    path('master_buku/', getMasterbuku, name='master_buku'),
    path('master_buku/tambah', formTambahbuku, name='tambah_buku'),
    path('master_buku/delete/<int:id>/', deleteBuku, name='delete_buku'),
    path('master_buku/edit/<int:id>/', formEditBuku, name='edit_buku'),
    # Sumber Buku
    path('master_sumber_buku/', getMastersumberbuku, name='master_sumber_buku'),
    path('master_sumber_buku/tambah', formTambahsumberbuku, name='tambah_sumber_buku'),
    path('master_sumber_buku/delete/<int:id>/', deleteSumberbuku, name='delete_sumber_buku'),
    path('master_sumber_buku/edit/<int:id_sumber>/', editSumberbuku, name='edit_sumber_buku'),
]
