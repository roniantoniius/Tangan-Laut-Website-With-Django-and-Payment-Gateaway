from django.forms import ModelForm
from django import forms
from tlaut_apps import *
from tlaut_apps.models import Donasi, LaporAksi

class FormDonasi(ModelForm):
    class Meta:
        model = Donasi
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Nama', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'email' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Email', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'nominal_id' : forms.Select({'class':'form-control', 'placeholder':"Nominal", 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'metode_id' : forms.Select({'class':'form-control', 'placeholder':'Metode Pembayaan', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'deskripsi' : forms.TextInput({'class':'form-control', 'placeholder':'Deskripsi', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
        }

class FormAksi(ModelForm):
    class Meta:
        model = LaporAksi
        fields = '__all__'

        widgets = {
            'kegiatan_id' : forms.Select({'class':'form-control', 'placeholder':"Jenis Kegiatan", 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'nama_komunitas' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Nama Komunitas', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'lokasi_aksi' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Lokasi Aksi', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'waktu_aksi' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Tanggal Aksi', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'deskripsi_aksi' : forms.Textarea({'class':'form-control', 'placeholder':'Deskripsi Seluruh Aksi', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'perkem_aksi' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Perkembangan Aksi Pertama', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'perkem_dana' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Prakiraan Dana Keluar Aksi Pertama', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'perkem_deskripsi' : forms.TextInput({'class':'form-control', 'placeholder':'Deskripsi Perkembangan Aksi Pertama', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'perkem_aksi2' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Perkembangan Aksi Kedua', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'perkem_dana2' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Prakiraan Dana Keluar Aksi Kedua', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'perkem_deskripsi2' : forms.TextInput({'class':'form-control', 'placeholder':'Deskripsi Perkembangan Aksi Pertama', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
            'perk_dana_total' : forms.TextInput({'class':'form-control form-control-lg', 'placeholder':'Prakiraan Dana Total', 'required':'required', 'style': 'margin-top: 2px; font-weight: 400; font-family: "Poppins";'}),
        }