from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect
import requests
from .decorators import check_recaptcha
from .models import UserProfile, User
from django.contrib.auth.decorators import login_required


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("landingpage"))
    return render(request, "pemilu/landing.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "pemilu/login.html", {
                "message": "Tidak Ditemukan"
            })
    return render(request, "pemilu/login.html")


def logout_view(request):
    logout(request)
    return render(request, "pemilu/login.html", {
        "message": "Keluar"
    })


@login_required
def verifikasi(request):
    if request.method == 'POST':

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        if result['success']:
            return redirect('/vote')
        else:
            return render(request, "pemilu/vote.html", {
                "message": "Captcha Salah"
            })

    return render(request, "pemilu/vote.html")


@login_required
@check_recaptcha
def vote(request):
    try:
            u = User.objects.get(username=f"{request.user.username}")
            UserProfile.objects.get(user=u)
            return redirect("/sesudah")
    except:
            return render(request, "pemilu/kartu.html")

@login_required
def kenali(request):
    return render(request, "pemilu/kenali.html")


@login_required
def visi1(request):
    return render(request, "pemilu/visi1.html")


@login_required
def visi2(request):
    return render(request, "pemilu/visi2.html")

@login_required
def visi3(request):
    return render(request, "pemilu/visi3.html")

@login_required
def visi4(request):
    return render(request, "pemilu/visi4.html")

@login_required
def tentukan(request):
    try:
            u = User.objects.get(username=f"{request.user.username}")
            UserProfile.objects.get(user=u)
            return redirect("/sesudah")
    except:
            return render(request, "pemilu/kartu.html")

@login_required
def konfirmasi(request):
    if request.method == "POST":
        u = User.objects.get(username=f"{request.user.username}")
        Post = UserProfile()
        Post.user = u
        Post.pilihan = 1
        Post.checklist = True
        Post.save()
        return redirect("/sesudah")
    else:
        try:
            u = User.objects.get(username=f"{request.user.username}")
            UserProfile.objects.get(user=u)
            return redirect("/sesudah")
        except:
            return render(request, "pemilu/confirmation.html")

@login_required
def konfirmasi2(request):
    if request.method == "POST":
        u = User.objects.get(username=f"{request.user.username}")
        Post = UserProfile()
        Post.user = u
        Post.pilihan = 2
        Post.checklist = True
        Post.save()
        return redirect("/sesudah")
    else:
        try:
            u = User.objects.get(username=f"{request.user.username}")
            UserProfile.objects.get(user=u)
            return redirect("sesudah")
        except:
            return render(request, "pemilu/confirmation2.html")

@login_required
def konfirmasi3(request):
    if request.method == "POST":
        u = User.objects.get(username=f"{request.user.username}")
        Post = UserProfile()
        Post.user = u
        Post.pilihan = 3
        Post.checklist = True
        Post.save()
        return redirect("/sesudah")
    else:
        try:
            u = User.objects.get(username=f"{request.user.username}")
            UserProfile.objects.get(user=u)
            return redirect("sesudah")
        except:
            return render(request, "pemilu/confirmation3.html")

@login_required
def konfirmasi4(request):
    if request.method == "POST":
        u = User.objects.get(username=f"{request.user.username}")
        Post = UserProfile()
        Post.user = u
        Post.pilihan = 4
        Post.checklist = True
        Post.save()
        return redirect("/sesudah")
    else:
        try:
            u = User.objects.get(username=f"{request.user.username}")
            UserProfile.objects.get(user=u)
            return redirect("/sesudah")
        except:
            return render(request, "pemilu/confirmation4.html")

def landingpage(request):
    return render(request, "pemilu/home.html")
    
@login_required
def sesudah(request):
    return render(request, "pemilu/harapan.html")

@login_required
def slamanesmalane(request):
    return render(request, "pemilu/slamane.html")

@login_required
def terimakasih(request):
    return render(request, "pemilu/terimakasih.html")

@login_required
def count(request):
    satu = UserProfile.objects.filter(pilihan=1)
    dua = UserProfile.objects.filter(pilihan=2)
    tiga = UserProfile.objects.filter(pilihan=3)
    empat = UserProfile.objects.filter(pilihan=4)
    lima = UserProfile.objects.filter(pilihan=5)
    sdh = UserProfile.objects.all()
    return render(request, "pemilu/count.html", {
                    "satu": len(satu),
                    "dua": len(dua),
                    "tiga": len(tiga),
                    "empat": len(empat),
                    "lima": len(lima),
                    "sdhs": sdh
                })


@login_required
def testing(request):
    u = User.objects.get(username=f"{request.user.username}")
    return HttpResponse("hello " + str(u))