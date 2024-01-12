from django.db import models

# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=64)
    release_date=models.IntegerField()
    director=models.CharField(max_length=32)
    actor=models.CharField(max_length=64)
    choice_list=[
            ('액션','액션'),
            ('범죄','범죄'),
            ('SF','SF'),
            ('코미디','코미디'),
            ('로맨스','로맨스'),
            ('스릴러','스릴러'),
            ('전쟁','전쟁'),
            ('공포','공포'),
            ('기타','기타'),
    ]
    genre=models.CharField(
        max_length=10,
        choices=choice_list,
        default='else'
    )
    stars=models.DecimalField(max_digits=3, decimal_places=1)
    running_time=models.IntegerField()
    review=models.TextField()
    image=models.FileField(upload_to='static/images')
