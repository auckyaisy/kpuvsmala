from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path("verifikasi/", views.verifikasi, name="verifikasi"),
    path("vote/", views.vote, name="vote"),
    path("kenali/", views.kenali, name="kenali"),
    path("visi/0/", views.visi, name="visi"),
    path("visi/1/", views.visi1, name="visi1"),
    path("visi/2/", views.visi2, name="visi2"),
    path("visi/3/", views.visi3, name="visi3"),
    path("visi/4/", views.visi4, name="visi4"),
    path("tentukan/", views.tentukan, name="tentukan"), 
    path("landingpage/", views.landingpage, name="landingpage"), 
    path("konfirmasi/0/", views.konfirmasi, name="konfirmasi"),
    path("konfirmasi/1/", views.konfirmasi1, name="konfirmasi1"),
    path("konfirmasi/2/", views.konfirmasi2, name="konfirmasi2"),
    path("konfirmasi/3/", views.konfirmasi3, name="konfirmasi3"),
    path("testing/", views.testing, name="testing"),
    path("sesudah/", views.sesudah, name="sesudah"),
    path("slamanesmalane/", views.slamanesmalane, name="slamanesmalane"),
    path("terimakasih/", views.terimakasih, name="terimakasih"),
    path("count/", views.count, name="count"),
    path("konfirmasi/4/", views.konfirmasi4, name="konfirmasi4")
]
