from django.db import models

# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=64)
    release_date=models.IntegerField()
    director=models.CharField(max_length=32)
    actor=models.CharField(max_length=64)
    genre=models.CharField(max_length=32)
    stars=models.DecimalField(max_digits=3, decimal_places=1)
    running_time=models.IntegerField()
    review=models.TextField()
    image=models.FileField(upload_to='static/images')
