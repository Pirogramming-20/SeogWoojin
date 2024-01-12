from django import forms

from .models import *

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('title', 'release_date','director','actor','genre','stars','running_time','review',)