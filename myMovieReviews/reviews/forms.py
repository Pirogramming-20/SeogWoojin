from django import forms

from .models import *

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'release_date','genre','stars','running_time','review','director','actor',)
        
        labels = {
            "title": "제목",
            'release_date':"개봉년도",
            'actor':'배우',
            'stars':'별점',
            'running_time':'러닝타임',
            'director':'감독',
            'genre':'장르',
            "review": "리뷰",
        }