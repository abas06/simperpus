from django import forms
from .models import *

class MasterBukuForm(forms.ModelForm):
    class Meta:
        model = MasterBuku
        fields = ['nama_buku', 'penulis', 'sumber_buku', 'harga_beli', 'harga_jual', 'harga_sewa']
        
class MasterSumberBukuForm(forms.ModelForm):
    class Meta:
        model = MasterSumberBuku
        fields = ['sumber']
        
class TransaksiKunjunganForm(forms.ModelForm):
    class Meta:
        model = TransaksiKunjungan
        fields = ['member_id', 'jenis_transaksi']
        
class MasterMemberForm(forms.ModelForm):
    class Meta:
        model = MasterMember
        fields = ['no_member', 'jenis_identitas', 'no_identitas', 'nama', 'alamat_ktp', 'domisili']
        
class BillingKasirForm(forms.ModelForm):
    class Meta:
        model = BillingKasir
        fields = ['kunjungan_id', 'no_billing', 'total_billing']
        
class BillingKasirDetailForm(forms.ModelForm):
    class Meta:
        model = BillingKasirDetail
        fields = ['buku_id', 'jenis_transaksi', 'qty', 'hari_peminjaman', 'harga']