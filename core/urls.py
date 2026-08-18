from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),


    path(
        "qrcode/",
        views.qrcode_page,
        name="qrcode"
    ),

    path(
        "qr-image/",
        views.qr_image,
        name="qr_image"
    ),
]