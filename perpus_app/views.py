from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader
import psycopg2
from django.conf import settings
from .forms import *
from .models import *

# Koneksi ke database

def dbconnection():
    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )
    cursor = conn.cursor()
    return conn, cursor

# Beranda
def beranda(request):
    return render (request, 'index.html')

# Master Buku
def getMasterbuku(request):
    conn, cursor = dbconnection()

    search_query = request.GET.get('q', '')
    source_query = request.GET.get('source', '')
    filter_query = ""

    if search_query:
        filter_query += f" AND a.nama_buku ILIKE '%%{search_query}%%'"
    if source_query:
        filter_query += f" AND a.sumber_buku_id = {source_query}"

    query = f"""
        SELECT a.id, a.nama_buku, a.penulis, b.sumber, a.harga_beli, a.harga_jual
        FROM master_buku a
        LEFT JOIN master_sumber_buku b ON b.id_sumber = a.sumber_buku_id
        WHERE a.is_deleted = 'false' {filter_query}
        ORDER BY a.id DESC
    """
    cursor.execute(query)
    list_buku = cursor.fetchall()

    cursor.execute("SELECT id_sumber, sumber FROM master_sumber_buku WHERE is_deleted = 'false'")
    sumber_buku_list = cursor.fetchall()

    cursor.close()
    conn.close()

    paginator = Paginator(list_buku, 10)  # 10 data per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'master_buku.html'
    context = {
        'list_buku': list_buku,
        'page_obj': page_obj,
        'search_query': search_query,
        'source_query': source_query,
        'sumber_buku_list': sumber_buku_list,
    }
    return render(request, template, context)

def formTambahbuku(request):
    
    list_sumber = MasterSumberBuku.objects.filter(is_deleted=False).values_list('id_sumber', 'sumber')
    
    if request.method == 'POST':
        form = MasterBukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('master_buku')
    else:
        form = MasterBukuForm()
    return render(request, 'tambah_buku.html', {'form': form, 'list_sumber': list_sumber})

def deleteBuku(request, id):
    buku = get_object_or_404(MasterBuku, id=id)
    buku.is_deleted = True
    buku.save()
    return redirect('master_buku')

def formEditBuku(request, id):
    buku = get_object_or_404(MasterBuku, id=id)
    list_sumber = MasterSumberBuku.objects.filter(is_deleted=False).values_list('id_sumber', 'sumber')
    
    if request.method == 'POST':
        form = MasterBukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('master_buku')
    else:
        form = MasterBukuForm(instance=buku)
    return render(request, 'edit_buku.html', {'form': form, 'list_sumber': list_sumber, 'buku': buku})

# Master Sumber Buku
def formTambahsumberbuku(request):
    if request.method == 'POST':
        form = MasterSumberBukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('master_sumber_buku')
    else:
        form = MasterBukuForm()
    return render(request, 'tambah_sumber_buku.html', {'form': form})

def getMastersumberbuku(request):
    search_query = request.GET.get('q', '')
    filter_query = ""

    if search_query:
        filter_query += f" AND sumber ILIKE '%%{search_query}%%'"

    conn, cursor = dbconnection()
    query = f"""
        SELECT * FROM master_sumber_buku
        WHERE is_deleted = 'false'
        {filter_query}
    """
    cursor.execute(query)
    list_sumber_buku = cursor.fetchall()
    cursor.close()
    conn.close()

    paginator = Paginator(list_sumber_buku, 10)  # 10 data per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'master_sumber_buku.html'
    context = {
        'list_sumber_buku': page_obj.object_list,  # Hanya data untuk halaman saat ini
        'page_obj': page_obj,
        'search_query': search_query
    }
    return render(request, template, context)

def deleteSumberbuku(request, id):
    buku = get_object_or_404(MasterSumberBuku, id_sumber=id)
    buku.is_deleted = True
    buku.save()
    return redirect('master_sumber_buku')

def editSumberbuku(request, id_sumber):
    sumber_buku = get_object_or_404(MasterSumberBuku, id_sumber=id_sumber)
    
    if request.method == 'POST':
        form = MasterSumberBukuForm(request.POST, instance=sumber_buku)
        if form.is_valid():
            form.save()
            return redirect('master_sumber_buku')
    else:
        form = MasterSumberBukuForm(instance=sumber_buku)
    
    return render(request, 'edit_sumber_buku.html', {'form': form, 'sumber_buku': sumber_buku})

# Master Buku

def getMastermember(request):
    conn, cursor = dbconnection()

    search_query = request.GET.get('q', '')
    filter_query = ""

    if search_query:
        filter_query += f" AND nama ILIKE '%%{search_query}%%'"

    query = f"""
        select * from master_member
        WHERE is_deleted = 'false' {filter_query}
        ORDER BY id DESC
    """
    cursor.execute(query)
    list_member = cursor.fetchall()

    cursor.close()
    conn.close()

    paginator = Paginator(list_member, 10)  # 10 data per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    template = 'master_member.html'
    context = {
        'list_member': list_member,
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, template, context)

def deleteMember(request, id):
    member = get_object_or_404(MasterMember, id=id)
    member.is_deleted = True
    member.save()
    return redirect('master_member')