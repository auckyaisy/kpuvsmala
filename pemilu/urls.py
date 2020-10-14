from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path("peserta/", views.peserta, name="peserta"),
    path("calon/", views.calon, name="calon"),
    path("verifikasi/", views.verifikasi, name="verifikasi"),
    path("vote/", views.vote, name="vote"),
    path("kenali/", views.kenali, name="kenali"),
    path("visi1/", views.visi1, name="visi1"),
    path("visi2/", views.visi2, name="visi2"),
    path("visi3/", views.visi3, name="visi3"),
    path("visi4/", views.visi4, name="visi4"),
    path("tentukan/", views.tentukan, name="tentukan"), 
    path("landingpage/", views.landingpage, name="landingpage"), 
    path("konfirmasi/", views.konfirmasi, name="konfirmasi"),
    path("konfirmasi2/", views.konfirmasi2, name="konfirmasi2"),
    path("konfirmasi3/", views.konfirmasi3, name="konfirmasi3"),
    path("testing/", views.testing, name="testing"),
    path("sesudah/", views.sesudah, name="sesudah"),
    path("slamanesmalane/", views.slamanesmalane, name="slamanesmalane"),
    path("terimakasih/", views.terimakasih, name="terimakasih"),
    path("count/", views.count, name="count"),
    path("konfirmasi4/", views.konfirmasi4, name="konfirmasi4")
]
