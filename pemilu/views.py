from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "pemilu/index.html")


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

def peserta(request):
    return render(request, "pemilu/peserta.html")

def calon(request):
    return render(request, "pemilu/calon.html")

def verifikasi(request):
    return render(request, "pemilu/vote.html")

def vote(request):
    return render(request, "pemilu/voting.html")

