from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path("peserta", views.peserta, name="peserta"),
    path("calon", views.calon, name="calon"),
    path("verifikasi", views.verifikasi, name="verifikasi"),
    path("vote", views.vote, name="vote"),
    path("loaderio-a4d352d8a6f3faa6ff162f58d006c23f/", views.loaderio, name="loaderio")
]
