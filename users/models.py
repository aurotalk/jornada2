from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    picture = models.ImageField('Foto de Perfil', default='/img/icone_vazio.png')
    following = models.ManyToManyField('self', blank=True)
    
