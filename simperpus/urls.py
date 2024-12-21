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
    # Master Buku
    path('master_buku/', getMasterbuku, name='master_buku'),
    path('master_buku/tambah', formTambahbuku, name='tambah_buku'),
    path('master_buku/delete/<int:id>/', deleteBuku, name='delete_buku'),
    path('master_buku/edit/<int:id>/', formEditBuku, name='edit_buku'),
    # Sumber Buku
    path('master_sumber_buku/', getMastersumberbuku, name='master_sumber_buku'),
    path('master_sumber_buku/tambah', formTambahsumberbuku, name='tambah_sumber_buku'),
    path('master_sumber_buku/delete/<int:id>/', deleteSumberbuku, name='delete_sumber_buku'),
    path('master_sumber_buku/edit/<int:id_sumber>/', editSumberbuku, name='edit_sumber_buku'),
    # Master Member
    path('master_member/', getMastermember, name='master_member'),
    path('master_member/delete/<int:id>/', deleteMember, name='delete_member'),
    # Transaksi Peminjaman
    path('reg_new_member', regNewmember, name='reg_new_member'),
    path('reg_old_member', regOldmember, name='reg_old_member'),
    path('autocomplete-members/', autocomplete_members, name='autocomplete-members'),
    path('reg_new_member/delete/<int:id>/', deleteTransaksi, name='delete_transaksi'),
    path('list_pengunjung', listPengunjung, name='list_pengunjung'),
    path('tambah_transaksi_buku/<int:id>', tambahtransaksiBuku, name='tambah_transaksi_buku'),
]
