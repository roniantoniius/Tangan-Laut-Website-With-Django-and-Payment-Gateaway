from django.contrib import admin
from tlaut_apps import *
from tlaut_apps.models import *
from .forms import *

# Register your models here.
from .models import *

class DonasiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'email', 'waktu', 'deskripsi']
    search_fields = ['nama', 'email', 'waktu', 'deskripsi']
    list_filter = ['nominal_id']
    list_per_page = 4

class AksiAdmin(admin.ModelAdmin):
    list_display = ['nama_komunitas', 'lokasi_aksi', 'waktu_aksi', 'deskripsi_aksi', 'perkem_aksi', 'perkem_dana', 'perkem_deskripsi', 'perkem_aksi2', 'perkem_dana2', 'perkem_deskripsi2', 'perk_dana_total']
    search_fields = ['nama_komunitas', 'lokasi_aksi', 'waktu_aksi', 'perk_dana_total']
    list_filter = ['kegiatan_id']
    list_per_page = 5

admin.site.register(Donasi, DonasiAdmin)
admin.site.register(Nominal)
admin.site.register(Metode)

admin.site.register(LaporAksi, AksiAdmin)
admin.site.register(Kegiatan)