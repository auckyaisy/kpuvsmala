from django.db import models


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  kelas = models.IntegerField(null=True)
  pararel = models.IntegerField(null=True)
  absen = models.IntegerField(null=True)

# Create your models here.
class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pilihan = models.IntegerField()
    checklist = models.BooleanField()

    def __str__(self):
        return f" {self.user} | {self.user.last_name} | {self.user.kelas}-{self.user.pararel}  {self.user.absen}" 

class Pilih(models.Model):
  id=models.AutoField(primary_key=True)
  pilihan = models.CharField(max_length=50,verbose_name="Pilihan")
  token = models.CharField(max_length=50,null=True,verbose_name="token")
  
  def __str__(self):
    return self.pilihan