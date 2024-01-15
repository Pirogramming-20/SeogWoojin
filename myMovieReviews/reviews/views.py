from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def review_list(request):
    sort = request.GET.get('sort','')
    if sort == 'title':
        content_list = Review.objects.all().order_by('title')
    elif sort ==  'years':
        content_list = Review.objects.all().order_by('-release_date')
    else:
        content_list = Review.objects.all().order_by('-stars')    
    context={
        "reviews":content_list
    }
    return render(request, 'review_list.html', context)

def review_create(request):
    if request.method=="POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.image=f"static/images/{review.title}.jpg"
            review.save()
            return redirect(f"/reviews/detail/{review.pk}")
    else:
        form = ReviewForm()
        return render(request, 'review_create.html', {'form':form})
    
def review_detail(request, pk):
    review=Review.objects.get(id=pk)
    hours=0
    minutes=0
    hour=False
    if review.running_time>=60:
        hours=review.running_time//60
        minutes=review.running_time%60
        hour=True
    content={
        "review":review,
        "hour":hour,
        "hours":hours,
        "minutes":minutes,
        
    }
    return render(request, 'review_detail.html', content)

def review_update(request,pk):
    review= Review.objects.get(id=pk)
    if request.method=="POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review.image=f"static/images/{review.title}.jpg"
            form.save()
            return redirect(f"/reviews/detail/{pk}")
    form=ReviewForm(instance=review)
    return render(request, 'review_update.html', {'form':form})

def review_delete(request,pk):
    if request.method=="POST":
        review=Review.objects.get(id=pk)
        review.delete()
        return redirect('/reviews')
    return redirect("/reviews")
        