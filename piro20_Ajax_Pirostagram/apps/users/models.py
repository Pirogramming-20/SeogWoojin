from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image=models.ImageField('이미지', blank=True, upload_to='users/%Y%m%d')
    name = models.CharField(max_length=10, null=False)


    def __str__(self):
        return self.name