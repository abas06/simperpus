from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import psycopg2
from django.conf import settings
from .forms import *
from .models import *
from django.db.models import Max
from django.utils import timezone
from datetime import datetime, timedelta
from django.http import JsonResponse

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

# Generator
def generate_no_member():
    last_member = MasterMember.objects.all().order_by('id').last()
    if not last_member:
        return 'MBR0001'
    
    last_no_member = last_member.no_member
    new_no = int(last_no_member[3:]) + 1
    new_no_member = f'MBR{new_no:04d}'
    return new_no_member

def generate_no_transaksi():
    today = timezone.now().strftime('%y%m%d')  
    last_transaksi = TransaksiKunjungan.objects.filter(
        tgl_transaksi__date=timezone.now().date() 
    ).order_by('id').last()

    if not last_transaksi:
        return f'TR{today}0001'

    last_no_transaksi = last_transaksi.no_transaksi
    last_sequence = int(last_no_transaksi[8:])
    new_sequence = last_sequence + 1 
    new_no_transaksi = f'TR{today}{new_sequence:04d}' 
    return new_no_transaksi

# Reg new member
def regNewmember(request):
    conn, cursor = dbconnection()
    if request.method == 'POST':
        member_form = MasterMemberForm(request.POST)
        transaksi_form = TransaksiKunjunganForm(request.POST)
        
        if member_form.is_valid() and transaksi_form.is_valid():
            local_time = timezone.localtime(timezone.now()) + timedelta(hours=7)
            formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
            new_no_member = generate_no_member()
            # Simpan data member baru
            new_member = member_form.save(commit=False)
            new_member.no_member = new_no_member
            new_member.status_aktif = True  # Atur status_aktif ke True
            new_member.save()
            
            new_no_transaksi = generate_no_transaksi()
            new_transaksi = transaksi_form.save(commit=False)
            new_transaksi.member_id = new_member
            new_transaksi.no_transaksi = new_no_transaksi
            new_transaksi.tgl_transaksi = formatted_time
            new_transaksi.jenis_kunjungan = 1
            new_transaksi.save()
            
            return redirect('reg_new_member')
        
    else:
        member_form = MasterMemberForm()
        transaksi_form = TransaksiKunjunganForm()
    
    search_query = request.GET.get('q', '')
    filter_query = ""
    
    if search_query:
        filter_query += f" AND b.nama ILIKE '%%{search_query}%%'"
        
    query = f"""
        SELECT a.id, a.no_transaksi, b.nama, 
        CASE 
            WHEN a.jenis_kunjungan = 1 THEN 'Kunjungan Baru'
            WHEN a.jenis_kunjungan = 2 THEN 'Kunjungan Lama'
        END AS jenis_kunjungan,
        CASE 
            WHEN a.jenis_transaksi = 1 THEN 'Peminjaman'
            WHEN a.jenis_transaksi = 2 THEN 'Pembelian'
            WHEN a.jenis_transaksi = 3 THEN 'Kunjungan'
        END AS jenis_transaksi
        FROM transaksi_kunjungan a
        LEFT JOIN master_member b ON b.id = a.member_id
        WHERE a.is_deleted = 'false' AND DATE(a.tgl_transaksi) = current_date
        {filter_query} order by a.id desc
    """
    cursor.execute(query)
    list_transaksi = cursor.fetchall()
    cursor.close()
    conn.close()
    
    paginator = Paginator(list_transaksi, 7)  # 10 data per halaman (disarankan lebih dari 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    context = {
        'member_form': member_form,
        'transaksi_form': transaksi_form,
        'page_obj': page_obj,
        'search_query': search_query,
        'list_transaksi': list_transaksi,
    }
    template = 'reg_new_member.html'
    return render(request, template, context)

def autocomplete_members(request):
    if 'term' in request.GET:
        # Ambil saran berdasarkan nama atau nomor member yang cocok dengan input
        qs = MasterMember.objects.filter(nama__icontains=request.GET.get('term'), is_deleted=False)
        members = list(qs.values('id', 'no_member', 'nama', 'domisili', 'no_identitas', 'alamat_ktp'))
        return JsonResponse(members, safe=False)
    return JsonResponse([], safe=False)

def regOldmember(request):
    list_member = MasterMember.objects.filter(is_deleted=False).values_list('id', 'no_member', 'nama')
    conn, cursor = dbconnection()
    if request.method == 'POST':
        transaksi_form = TransaksiKunjunganForm(request.POST)
        if transaksi_form.is_valid():
            local_time = timezone.localtime(timezone.now()) + timedelta(hours=7)
            formatted_time = local_time.strftime('%Y-%m-%d %H:%M:%S')
            new_no_transaksi = generate_no_transaksi()
            new_transaksi = transaksi_form.save(commit=False)
            new_transaksi.no_transaksi = new_no_transaksi
            new_transaksi.tgl_transaksi = formatted_time
            new_transaksi.jenis_kunjungan = 2
            transaksi_form.save()
            return redirect('reg_old_member')
    else:
        transaksi_form = TransaksiKunjunganForm()

    search_query = request.GET.get('q', '')
    filter_query = ""

    if search_query:
        filter_query += f" AND b.nama ILIKE '%%{search_query}%%'"

    query = f"""
        SELECT a.id, a.no_transaksi, b.nama, 
        CASE 
            WHEN a.jenis_kunjungan = 1 THEN 'Kunjungan Baru'
            WHEN a.jenis_kunjungan = 2 THEN 'Kunjungan Lama'
        END AS jenis_kunjungan,
        CASE 
            WHEN a.jenis_transaksi = 1 THEN 'Peminjaman'
            WHEN a.jenis_transaksi = 2 THEN 'Pembelian'
            WHEN a.jenis_transaksi = 3 THEN 'Kunjungan'
        END AS jenis_transaksi
        FROM transaksi_kunjungan a
        LEFT JOIN master_member b ON b.id = a.member_id
        WHERE a.is_deleted = 'false' AND DATE(a.tgl_transaksi) = current_date
        {filter_query} order by a.id desc
    """
    cursor.execute(query)
    list_transaksi = cursor.fetchall()
    cursor.close()
    conn.close()

    paginator = Paginator(list_transaksi, 7)  # 10 data per halaman (disarankan lebih dari 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'transaksi_form': transaksi_form,
        'list_member': list_member,
        'page_obj': page_obj,
        'search_query': search_query,
        'list_transaksi': list_transaksi
    }
    template = 'reg_old_member.html'
    return render(request, template, context)

def deleteTransaksi(request, id):
    list_transaksi = get_object_or_404(TransaksiKunjungan, id=id)
    list_transaksi.is_deleted = True
    list_transaksi.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
