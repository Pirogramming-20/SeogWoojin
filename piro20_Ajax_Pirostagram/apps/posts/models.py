from django.db import models
from apps.users.models import User

class Post(models.Model):
    image=models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    content=models.TextField('내용',max_length=100)
    heart=models.ManyToManyField(User, related_name="heart_user")
    created_date=models.DateTimeField("작성일", auto_created=True, auto_now_add=True)
    updated_date=models.DateTimeField("수정일", auto_created=True, auto_now=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성유저')

class Comment(models.Model):
    comment_user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="댓글 작성 유저")
    content=models.CharField(max_length=50, null=False)
    post=models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="게시글")
    
# Create your models here.
