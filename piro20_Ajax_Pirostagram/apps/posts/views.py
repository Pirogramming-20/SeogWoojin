from django.shortcuts import render,redirect
from .models import *
from .forms import PostForm
import json
from django.http import JsonResponse

# Create your views here.
def main(request):
    posts=Post.objects.all()
    print(posts[0].comment_set.all())
    return render(request, "posts/main.html", {'posts':posts})

def create(request):
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            post=form.save(commit=False)
            post.user=request.user
            post.save()
        return redirect('posts:main')
    
    form=PostForm()
    return render(request, "posts/create.html", {'form':form})
    
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def write_comment(request):
    if request.method=="POST":
        req=json.loads(request.body)
        post_id=req['id']
        comment=req['comment']
        print(post_id, comment)
        user=request.user
        print(type(user))
        post=Post.objects.get(id=post_id)
        
        new_comment=Comment.objects.create(content=comment, comment_user=user, post=post )
        user.comment=new_comment
        post.comment=new_comment
        post.save()
        user.save()
        print(user.comment)
        return JsonResponse({'id':post_id, 'text':comment})