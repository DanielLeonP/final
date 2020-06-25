from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares/', default ='avatares/default.jpg')
    desc = models.TextField( default='Aún no hay una descripción disponible')
    def __str__(self):
        return "{} - {}".format(self.user,self.desc)