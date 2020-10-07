from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    pilihan = models.IntegerField()
    checklist = models.BooleanField()

    def __str__(self):
        return self.user.username
