from django.db import models

# Create your models here.

class Nominal(models.Model):
    biaya = models.CharField(max_length=20)
    def __str__(self):
        return self.biaya

class Metode(models.Model):
    bank = models.CharField(max_length=35)
    def __str__(self):
        return self.bank

class Kegiatan(models.Model):
    jenis_aksi = models.CharField(max_length=50)
    def __str__(self):
        return self.jenis_aksi

class Donasi(models.Model):
    nama = models.CharField(max_length=50)
    email = models.EmailField()
    waktu = models.DateTimeField(auto_now_add=True)
    deskripsi = models.TextField()

    nominal_id = models.ForeignKey(Nominal, on_delete=models.CASCADE, null=True)
    metode_id = models.ForeignKey(Metode, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nama

class LaporAksi(models.Model):
    nama_komunitas = models.CharField(max_length=50)
    kegiatan_id = models.ForeignKey(Kegiatan, on_delete=models.CASCADE, null=True)
    lokasi_aksi = models.CharField(max_length=50)
    waktu_aksi = models.CharField(max_length=50)
    perkem_aksi = models.CharField(max_length=50)
    perkem_dana = models.CharField(max_length=50)
    perkem_deskripsi = models.TextField()
    perkem_aksi2 = models.CharField(max_length=50)
    perkem_dana2 = models.CharField(max_length=50)
    perkem_deskripsi2 = models.TextField()
    perk_dana_total = models.CharField(max_length=50)
    deskripsi_aksi = models.TextField()
    
    def __str__(self):
        return self.nama_komunitas


def __str__(self):
        return self.biaya

def __str__(self):
        return self.bank

def __str__(self):
        return self.jenis_aksi