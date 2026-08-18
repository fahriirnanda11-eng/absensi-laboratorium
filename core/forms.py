from django import forms
from .models import Absensi

class AbsensiForm(forms.ModelForm):
    class Meta:
        model = Absensi
        fields = [
            "mata_kuliah",
            "nama_dosen",
            "nim",
            "nama",
            "prodi",
            "no_pc",
            "jam_mulai",
            "jam_selesai",
        ]

        widgets = {
            "mata_kuliah": forms.TextInput(attrs={"class": "form-control"}),
            "nama_dosen": forms.TextInput(attrs={"class": "form-control"}),
            "nim": forms.TextInput(attrs={"class": "form-control"}),
            "nama": forms.TextInput(attrs={"class": "form-control"}),
            "prodi": forms.Select(attrs={"class": "form-select"}),
            "no_pc": forms.TextInput(attrs={"class": "form-control"}),
            "jam_mulai": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "jam_selesai": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
        }