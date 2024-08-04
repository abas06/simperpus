from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
import psycopg2
from django.conf import settings
from .forms import *
from .models import *

# Koneksi ke database

def dbconnection():
    # Membuat koneksi ke database
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )
    
    # Membuat cursor untuk eksekusi query
    cursor = conn.cursor()
    
    return conn, cursor

# Create your views here.
def beranda(request):
    return render (request, 'index.html')

def formTambahbuku(request):
    
    list_sumber = MasterSumberBuku.objects.filter(is_deleted=False).values_list('id_sumber', 'sumber')
    
    if request.method == 'POST':
        form = MasterBukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('master_buku')  # Ubah ke URL tujuan Anda
        # else:
        #     print(form.errors)  # Cetak error form jika tidak valid
    else:
        form = MasterBukuForm()
    return render(request, 'tambah_buku.html', {'form': form, 'list_sumber': list_sumber})

def formTambahsumberbuku(request):
    if request.method == 'POST':
        form = MasterSumberBukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('master_sumber_buku')  # Ubah ke URL tujuan Anda
        # else:
        #     print(form.errors)  # Cetak error form jika tidak valid
    else:
        form = MasterBukuForm()
    return render(request, 'tambah_sumber_buku.html', {'form': form})


def getMasterbuku(request):
    conn, cursor = dbconnection()
    query = """ SELECT a.id, a.nama_buku, a.penulis, b.sumber, a.harga_beli, a.harga_jual
        FROM master_buku a
        LEFT JOIN master_sumber_buku b ON b.id_sumber = a.sumber_buku_id
        WHERE a.is_deleted = 'false'
        ORDER BY a.id DESC
    """
    cursor.execute(query)
    list_buku = cursor.fetchall()
    cursor.close()
    conn.close()
    template = 'master_buku.html'
    context = {'list_buku': list_buku}
    
    return render(request, template, context)

def getMastersumberbuku(request):
    conn, cursor = dbconnection()
    query = """ SELECT * FROM master_sumber_buku WHERE is_deleted = 'false'
    """
    cursor.execute(query)
    list_sumber_buku = cursor.fetchall()
    cursor.close()
    conn.close()
    template = 'master_sumber_buku.html'
    context = {'list_sumber_buku': list_sumber_buku}
    
    return render(request, template, context)

def delete_buku(request, id):
    buku = get_object_or_404(MasterBuku, id=id)
    buku.is_deleted = True
    buku.save()
    return redirect('master_buku')