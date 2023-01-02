from django.shortcuts import render, redirect, HttpResponse
import uuid
from .forms import *
import midtransclient
from django.conf import settings
from django.http import Http404
from django.http import HttpResponse
from tlaut_apps.constants import DUMMY_PRODUCTS, PAYMENT_STATUS
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def RelawanPage(request):
    return render(request, 'relawan.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('relawan')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def beranda(request):
        return render(request, "beranda.html")

def aksi(request):        
        return render(request, "aksi.html")

def dashadmin(request):
        return render(request, "dashadmin.html")       


def aksi2(request):
        judul = "Ini Judul"
        isi = "Ini Isi"

        konteks = {
                'judul' : judul,
                'isi' : isi,
        }
        
        return render(request, "aksi2.html", konteks)


def aksi3(request):
        judul = "Ini Judul"
        isi = "Ini Isi"

        konteks = {
                'judul' : judul,
                'isi' : isi,
        }
        
        return render(request, "aksi3.html", konteks)


def donasi_kelola(request):
    dona = Donasi.objects.all()
    judul = "Form Tambah data"
    konteks = {
        "Title" : judul,
        "subtitle" : judul,
        "donate" : dona,
    }
    return render(request, 'donasi_kelola.html', konteks)

def donasi(request):
    dona = Donasi.objects.all()
    if request.POST:
        form = FormDonasi(request.POST, request.FILES)
        if form.is_valid(): #ketika data dikirimkan
            form.save()
            judul = "Form Tambah data"
            pesan = "Data Berhasil Ditambahkan !"
            konteks = {
                "form" : form,
                "pesan" : pesan,
                'products': DUMMY_PRODUCTS,
            }
        return render(request, 'nominal.html', konteks)

    else:
        form = FormDonasi()
        dona = Donasi.objects.all()
        judul = "Form Tambah data"
        konteks = {
            "Title" : judul,
            "subtitle" : judul,
            "donate" : dona,
            "form" : form,
        }
    return render(request, 'donasi.html', konteks)

def donasi_update(request, id_donate):
    donas = Donasi.objects.get(id = id_donate)
    judul = "Update data donasi"
    template = "donasi_update.html"

    if request.POST:
        # memiliki intens (data sebelumnya)
        form = FormDonasi(request.POST, request.FILES, instance=donas)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate !"
            konteks = {
                "Title" : judul,
                "subtitle" : judul,
                "pesan" : pesan,
                "form" : form,
                "donas" : donas, #supaya data bisa ditampilkan
            }
            return render(request, template, konteks)

    else:
        form = FormDonasi(instance=donas)
        konteks = {
            "Title" : judul,
            "subtitle" : judul,
            "form" : form,
            "donas" : donas,
        }
    return render(request, template, konteks)

MIDTRANS_CORE = midtransclient.CoreApi(
    is_production=not settings.DEBUG,
    server_key=settings.MIDTRANS['SERVER_KEY'],
    client_key=settings.MIDTRANS['CLIENT_KEY'],
)

MIDTRANS_SNAP = midtransclient.Snap(
    is_production=not settings.DEBUG,
    server_key=settings.MIDTRANS['SERVER_KEY'],
    client_key=settings.MIDTRANS['CLIENT_KEY'],
)


def nominal(request):
    ctx = {
        'products': DUMMY_PRODUCTS
    }

    return render(request, 'nominal.html', ctx)


def checkout_view(request, product_id):
    try:
        product = [x for x in DUMMY_PRODUCTS if x.get('id') == product_id][0]
    except KeyError:
        raise Http404

    resp = MIDTRANS_CORE.charge({
        "payment_type": "bank_transfer",
        "transaction_details": {
            "order_id": uuid.uuid4().hex,  # mocked order id
            "gross_amount": product.get('price')
        },
        "bank_transfer": {
            "bank": "bca"
        },
        'metadata': {
            'product_id': product_id
        },
    })

    ctx = {
        'transaction_id': resp.get('transaction_id'),
        'amount': resp.get('gross_amount'),
        'status': PAYMENT_STATUS[resp.get('transaction_status')],
        'midtrans_status': resp.get('transaction_status'),
        'virtual_accounts': resp.get('va_numbers'),
        'product': product,
    }

    return render(request, 'payment.html', ctx)


def check_payment_info_view(request, reference_id):
    resp = MIDTRANS_CORE.transactions.status(reference_id)

    product_id = resp.get('metadata').get('product_id')

    try:
        product = [x for x in DUMMY_PRODUCTS if x.get('id') == product_id][0]
    except KeyError:
        raise Http404

    ctx = {
        'transaction_id': reference_id,
        'amount': resp.get('gross_amount'),
        'status': PAYMENT_STATUS[resp.get('transaction_status')],
        'midtrans_status': resp.get('transaction_status'),
        'virtual_accounts': resp.get('va_numbers'),
        'product': product,
    }

    return render(request, 'payment.html', ctx)
# Create your views here.


def donasi_hapus(request, id_donate):
    donas = Donasi.objects.get(id = id_donate)
    #melakukan redirect
    donas.delete()

    return redirect("/donasi_kelola/")

@login_required(login_url='login')
def formaksi(request):
    if request.POST:
        form = FormAksi(request.POST, request.FILES)
        if form.is_valid(): #ketika data dikirimkan
            form.save()
            judul = "Form Tambah data"
            pesan = "Data Berhasil Ditambahkan !"
            konteks = {
                "Title" : judul,
                "subtitle" : judul,
                "form" : form,
                "pesan" : pesan,
            }
        return render(request, 'formaksi.html', konteks)

    else:
        form = FormAksi()
        action = LaporAksi.objects.all()
        judul = "Form Tambah data"
        konteks = {
            "Title" : judul,
            "subtitle" : judul,
            "act" : action,
            "form" : form,
        }
    return render(request, 'formaksi.html', konteks)

def aksi_kelola(request):
    action = LaporAksi.objects.all()
    judul = "Form Tambah data"
    konteks = {
        "Title" : judul,
        "subtitle" : judul,
        "act" : action,
    }
    return render(request, 'aksi_kelola.html', konteks)

def aksi_update(request, id_act):
    acid = LaporAksi.objects.get(id = id_act)
    judul = "Update data donasi"
    template = "aksi_update.html"

    if request.POST:
        # memiliki intens (data sebelumnya)
        form = FormAksi(request.POST, request.FILES, instance=acid)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate !"
            konteks = {
                "Title" : judul,
                "subtitle" : judul,
                "pesan" : pesan,
                "form" : form,
                "acid" : acid, #supaya data bisa ditampilkan
            }
            return render(request, template, konteks)

    else:
        form = FormAksi(instance=acid)
        konteks = {
            "Title" : judul,
            "subtitle" : judul,
            "form" : form,
            "acid" : acid,
        }
    return render(request, template, konteks)

def aksi_hapus(request, id_act):
    acid = LaporAksi.objects.get(id = id_act)
    #melakukan redirect
    acid.delete()

    return redirect("/aksi_kelola/")