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

captresult = False

def index(request):
    # if not request.user.is_authenticated:
        # return HttpResponseRedirect(reverse("landingpage"))
    return render(request, "pemilu/home.html")

def selesai(request):
    return render(request, 'pemilu/tutup.html')

def rekapitulasi(request):
    return render(request, "pemilu/rekap.html")
# def login_view(request):
#     if not request.user.is_authenticated:
#         if request.method == "POST":
#             username = request.POST["username"]
#             password = request.POST["password"]
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse("index"))
#             else:
#                 return render(request, "pemilu/login.html", {
#                     "message": "Tidak Ditemukan"
#                 })
#         return render(request, "pemilu/login.html")
#     else:
#         return redirect("/")


# def logout_view(request):
#     logout(request)
#     return render(request, "pemilu/login.html", {
#         "message": "Keluar"
#     })


# @login_required
# def verifikasi(request):
#     try:
#         u = User.objects.get(username=f"{request.user.username}")
#         UserProfile.objects.get(user=u)
#         return redirect("/sesudah")
#     except:
#         if request.method == 'POST':
#             ''' Begin reCAPTCHA validation '''
#             recaptcha_response = request.POST.get('g-recaptcha-response')
#             data = {
#                 'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
#                 'response': recaptcha_response
#             }
#             r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
#             result = r.json()
#             ''' End reCAPTCHA validation '''

#             if result['success']:
#                 global captresult
#                 captresult = True
#                 return redirect('/vote/')
#             else:
#                 return render(request, "pemilu/vote.html", {
#                     "message": "Captcha Salah"
#                 })
#         else:
#             return render(request, "pemilu/vote.html")


# @login_required
# @check_recaptcha
# def vote(request):
#     try:
#         u = User.objects.get(username=f"{request.user.username}")
#         UserProfile.objects.get(user=u)
#         return redirect("/sesudah")
#     except:
#         return render(request, "pemilu/kartu.html")

# @login_required
# def kenali(request):
#     return render(request, "pemilu/kenali.html")


# @login_required
# def visi1(request):
#     return render(request, "pemilu/page2.html")
    
# @login_required
# def visi(request):
#     return render(request, "pemilu/index.html")


# @login_required
# def visi2(request):
#     return render(request, "pemilu/page1.html")

# @login_required
# def visi3(request):
#     return render(request, "pemilu/page3.html")

# @login_required
# def visi4(request):
#     return render(request, "pemilu/page4.html")


# @login_required
# def tentukan(request):
#     try:
#             u = User.objects.get(username=f"{request.user.username}")
#             UserProfile.objects.get(user=u)
#             return redirect("/sesudah")
#     except:
#             return render(request, "pemilu/tentukan.html")

# @login_required
# def konfirmasi(request):
#     if request.method == "POST":
#         u = User.objects.get(username=f"{request.user.username}")
#         Post = UserProfile()
#         Post.user = u
#         Post.pilihan = 1
#         Post.checklist = True
#         Post.save()
#         return redirect("/sesudah")
#     else:
#         try:
#             u = User.objects.get(username=f"{request.user.username}")
#             UserProfile.objects.get(user=u)
#             return redirect("/sesudah")
#         except:
#             return render(request, "pemilu/confirmation.html")

# @login_required
# def konfirmasi1(request):
#     if request.method == "POST":
#         u = User.objects.get(username=f"{request.user.username}")
#         Post = UserProfile()
#         Post.user = u
#         Post.pilihan = 2
#         Post.checklist = True
#         Post.save()
#         return redirect("/sesudah")
#     else:
#         try:
#             u = User.objects.get(username=f"{request.user.username}")
#             UserProfile.objects.get(user=u)
#             return redirect("/sesudah")
#         except:
#             return render(request, "pemilu/confirmation2.html")

# @login_required
# def konfirmasi2(request):
#     if request.method == "POST":
#         u = User.objects.get(username=f"{request.user.username}")
#         Post = UserProfile()
#         Post.user = u
#         Post.pilihan = 3
#         Post.checklist = True
#         Post.save()
#         return redirect("/sesudah")
#     else:
#         try:
#             u = User.objects.get(username=f"{request.user.username}")
#             UserProfile.objects.get(user=u)
#             return redirect("sesudah")
#         except:
#             return render(request, "pemilu/confirmation4.html")

# @login_required
# def konfirmasi3(request):
#     if request.method == "POST":
#         u = User.objects.get(username=f"{request.user.username}")
#         Post = UserProfile()
#         Post.user = u
#         Post.pilihan = 4
#         Post.checklist = True
#         Post.save()
#         return redirect("/sesudah")
#     else:
#         try:
#             u = User.objects.get(username=f"{request.user.username}")
#             UserProfile.objects.get(user=u)
#             return redirect("sesudah")
#         except:
#             return render(request, "pemilu/confirmation3.html")

# @login_required
# def konfirmasi4(request):
#     if request.method == "POST":
#         u = User.objects.get(username=f"{request.user.username}")
#         Post = UserProfile()
#         Post.user = u
#         Post.pilihan = 5
#         Post.checklist = True
#         Post.save()
#         return redirect("/sesudah")
#     else:
#         try:
#             u = User.objects.get(username=f"{request.user.username}")
#             UserProfile.objects.get(user=u)
#             return redirect("/sesudah")
#         except:
#             return render(request, "pemilu/confirmation5.html")

# def landingpage(request):
#     return render(request, "pemilu/home.html")
    
# @login_required
# def sesudah(request):
#     return render(request, "pemilu/harapan.html")

# @login_required
# def slamanesmalane(request):
#     if request.method == "POST":
#         logout(request)
#         return redirect("https://www.instagram.com/mediasmalane")
#     else:
#         return render(request, "pemilu/slamane.html")

# @login_required
# def terimakasih(request):
#     return render(request, "pemilu/terimakasih.html")

# @login_required
# def saran(request):
#     return render(request, "pemilu/saran.html")

# @login_required
# def hasil(request):
#     satu = UserProfile.objects.filter(pilihan=1)
#     dua = UserProfile.objects.filter(pilihan=2)
#     tiga = UserProfile.objects.filter(pilihan=3)
#     empat = UserProfile.objects.filter(pilihan=4)
#     lima = UserProfile.objects.filter(pilihan=5)
#     sdh = UserProfile.objects.all()
#     return render(request, "pemilu/hasil.html", {
#                     "satu": len(satu),
#                     "dua": len(dua),
#                     "tiga": len(tiga),
#                     "empat": len(empat),
#                     "lima": len(lima),
#                     "sdhs": sdh
#                 })

# @login_required
# def count(request):
#     # satu = UserProfile.objects.filter(pararel=1)
#     # dua = UserProfile.objects.filter(pararel=1)
#     # tiga = UserProfile.objects.filter(pararel=1)
#     # empat = UserProfile.objects.filter(pararel=1)
#     # lima = UserProfile.objects.filter(pararel=1)
#     # enam = UserProfile.objects.filter(pararel=1)
#     # tujuh = UserProfile.objects.filter(pararel=1)
#     # lapan = UserProfile.objects.filter(pararel=1)
#     # sembilan = UserProfile.objects.filter(pararel=1)
#     # sepuluh = UserProfile.objects.filter(pararel=1)
#     # x = UserProfile.objects.filter(kelas=10)
#     # xi = UserProfile.objects.filter(kelas=11)
#     # xii = UserProfile.objects.filter(kelas=12)
#     # g = UserProfile.objects.filter(kelas=5)
#     sdh = UserProfile.objects.all()
#     if request.method == "POST":
#         a = []
#         i = request.POST.get('kelas')
#         j = request.POST.get('pararel')
#         for k in range(1,65):
#             if i == 5:
#                 try:
#                     u = User.objects.get(kelas=5,pararel=0,absen=k)
#                     a.append(UserProfile.objects.get(user=u))
#                 except:
#                     pass
#             elif i == 6:
#                 try:
#                     u = User.objects.get(kelas=6,pararel=0,absen=k)
#                     a.append(UserProfile.objects.get(user=u))
#                 except:
#                     pass
#             else:
#                 try:
#                     u = User.objects.get(kelas=i, pararel=j,absen=k)
#                     a.append(UserProfile.objects.get(user=u))
#                 except:
#                     pass
#         return render(request, "pemilu/count.html", {
#             "sdhs": a,
#             "kelas": f"{i}",
#             "pararel": f"{j}"
#         })
#     # k = UserProfile.objects.filter(kelas=6)
#     return render(request, "pemilu/count.html", {
        
#                 })


# @login_required
# def testing(request):
#     u = User.objects.get(username=f"{request.user.username}")
#     return HttpResponse("hello " + str(u))