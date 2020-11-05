import csv, sys, os, django


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
from pemilu.models import User
# User = get_user_model()

file = 'import.csv'

data = csv.reader(open(file), delimiter=",")
for row in data:
    if row[0] != "Number":
        # Post.id = row[0]
        Post=User()
        Post.password = make_password(row[4])
        Post.last_login = "2020-09-28 05:51:42.521991"
        Post.is_superuser = "0"
        Post.username = row[3]
        Post.first_name = row[1]
        Post.is_staff = "0"
        Post.is_active = "1"
        Post.kelas = row[7]
        Post.pararel = row[6]
        Post.absen = row[5]
        Post.date_joined = "2020-09-28 05:51:42.521991"
        Post.last_name=row[2]
        Post.save()