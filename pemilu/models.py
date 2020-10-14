from django.db import models


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass

# Create your models here.
class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pilihan = models.IntegerField()
    checklist = models.BooleanField()

    def __str__(self):
        return f"{self.user}"
