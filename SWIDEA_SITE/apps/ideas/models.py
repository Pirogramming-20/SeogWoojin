from django.db import models
from apps.devtools.models import Devtool

# Create your models here.
class Idea(models.Model):
    title=models.CharField(max_length=24)
    image=models.ImageField('이미지', blank=True, upload_to='ideas/%Y%m%d')
    content=models.CharField(max_length=100)
    interest=models.IntegerField('좋아요',default=0)
    devtool=models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name='개발툴')
    created_date=models.DateTimeField("작성일", auto_created=True, auto_now_add=True)
    updated_date=models.DateTimeField("수정일", auto_created=True, auto_now=True)
    
class IdeaStar(models.Model):
    star=models.BooleanField(default=False)
    idea=models.OneToOneField(Idea, on_delete=models.CASCADE, related_name="ideastar")