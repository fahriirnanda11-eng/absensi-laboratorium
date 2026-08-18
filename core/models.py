from django.db import models

class Absensi(models.Model):
    PRODI = [
        ('TIF', 'Teknik Informatika'),
        ('SI', 'Sistem Informasi'),
        ('IK', 'Ilmu Komputer'),
    ]

    mata_kuliah = models.CharField(max_length=100)
    nama_dosen = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    prodi = models.CharField(max_length=20, choices=PRODI)
    no_pc = models.CharField(max_length=10)
    tanggal = models.DateField(auto_now_add=True)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nama} ({self.nim})"
    