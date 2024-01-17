from django.db import models

# Create your models here.
class Devtool(models.Model):
    name=models.CharField(max_length=24)
    kind=models.CharField(max_length=24)
    content=models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'