from django import forms
from .models import *

class MasterBukuForm(forms.ModelForm):
    class Meta:
        model = MasterBuku
        fields = ['nama_buku', 'penulis', 'sumber_buku', 'harga_beli', 'harga_jual']
        
class MasterSumberBukuForm(forms.ModelForm):
    class Meta:
        model = MasterSumberBuku
        fields = ['sumber']
