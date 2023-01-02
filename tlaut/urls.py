"""tlaut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from tlaut_apps.views import * #* artinya semua diambiil
from django.conf import settings
from tlaut_apps import views
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', beranda, name='beranda'),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('relawan/',views.RelawanPage,name='relawan'),
    path("donasi/", donasi),
    path("aksi/", aksi),
    path("aksi2/", aksi2),
    path("aksi3/", aksi3),
    path("nominal/", nominal),
    path("donasi_kelola/", donasi_kelola),
    path("aksi_kelola/", aksi_kelola),
    path("formaksi/", formaksi),
    path("dashadmin/", dashadmin),
    path('donasi_kelola/donasi_update/<int:id_donate>', donasi_update, name='donasi_update'),
    path('donasi_kelola/donasi_hapus/<int:id_donate>', donasi_hapus, name='donasi_hapus'),
    path('aksi_kelola/aksi_update/<int:id_act>', aksi_update, name='aksi_update'),
    path('aksi_kelola/aksi_hapus/<int:id_act>', aksi_hapus, name='aksi_hapus'),
    path('checkout/<product_id>', checkout_view, name='checkout'),
    path('payment-confirmation/<reference_id>', check_payment_info_view, name='payment-confirmation'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
