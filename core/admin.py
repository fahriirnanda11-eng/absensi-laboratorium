from django.contrib import admin
from django.http import HttpResponse
from openpyxl import Workbook
from .models import Absensi


def export_excel(modeladmin, request, queryset):
    wb = Workbook()
    ws = wb.active
    ws.title = "Data Absensi"

    ws.append([
        "Tanggal",
        "Jam Mulai",
        "Jam Selesai",
        "Mata Kuliah",
        "Nama Dosen",
        "NIM",
        "Nama Mahasiswa",
        "Prodi",
        "No PC",
    ])

    for obj in queryset:
        ws.append([
            str(obj.tanggal),
            str(obj.jam_mulai),
            str(obj.jam_selesai),
            obj.mata_kuliah,
            obj.nama_dosen,
            obj.nim,
            obj.nama,
            obj.prodi,
            obj.no_pc,
        ])

    response = HttpResponse(
        content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response["Content-Disposition"] = 'attachment; filename="Data_Absensi.xlsx"'

    wb.save(response)
    return response


export_excel.short_description = "Export ke Excel"


@admin.register(Absensi)
class AbsensiAdmin(admin.ModelAdmin):
    list_display = (
        "tanggal",
        "jam_mulai",
        "jam_selesai",
        "mata_kuliah",
        "nama_dosen",
        "nim",
        "nama",
        "prodi",
        "no_pc",
    )

    search_fields = (
        "nim",
        "nama",
        "mata_kuliah",
        "nama_dosen",
    )

    list_filter = (
        "tanggal",
        "mata_kuliah",
        "nama_dosen",
        "prodi",
        "jam_mulai",
    )

    ordering = (
        "-tanggal",
        "mata_kuliah",
        "jam_mulai",
        "nama",
    )

    date_hierarchy = "tanggal"

    actions = [export_excel]