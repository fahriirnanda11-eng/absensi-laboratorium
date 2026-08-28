from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

from io import BytesIO
import qrcode

from .forms import AbsensiForm
from .models import Absensi


def index(request):
    if request.method == "POST":
        form = AbsensiForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Absensi berhasil disimpan.")
            return redirect("index")
    else:
        form = AbsensiForm()

    jumlah_hari_ini = Absensi.objects.filter(
        tanggal=timezone.localdate()
    ).count()

    return render(
        request,
        "core/index.html",
        {
            "form": form,
            "jumlah": jumlah_hari_ini,
        },
    )



def qrcode_page(request):
    return render(request, "core/qrcode.html")


def qr_image(request):
    # Otomatis menggunakan alamat website yang sedang dibuka
    url = request.build_absolute_uri("/")

    img = qrcode.make(url)

    buffer = BytesIO()
    img.save(buffer, format="PNG")

    return HttpResponse(
        buffer.getvalue(),
        content_type="image/png"
    )