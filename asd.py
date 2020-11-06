import csv, sys, os, django
from time import sleep


project_dir = "/"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'kpuvsmala.settings'
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", __file__)
import django
django.setup()


from django.contrib.auth import authenticate
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


from django.contrib.auth import get_user_model
from django.conf import settings
from pemilu.models import User, Pilih
# User = get_user_model()

file = 'a.csv'

data = csv.reader(open(file), delimiter=",")
for row in data:
    if row[0] != "Number":
        # Post.id = row[0]
        Post=Pilih()
        Post.pilihan = row[0]
        Post.token = row[1]
        Post.save()
    sleep(2.4)