from django.shortcuts import render,redirect
from .models import *
from .forms import PostForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    posts=Post.objects.all()
    return render(request, "posts/main.html", {'posts':posts})

def create(request):
    if request.method=="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
        return redirect('posts:main')
    
    form=PostForm()
    return render(request, "posts/create.html", {'form':form})
    


@login_required
@csrf_exempt
def write_comment(request):
    if request.method=="POST":
        req=json.loads(request.body)
        post_id=req['id']
        comment=req['comment']
        user=request.user
        post=Post.objects.get(id=post_id)
        
        new_comment=Comment.objects.create(content=comment, comment_user=user, post=post )
        user.comment=new_comment
        post.comment=new_comment
        post.save()
        user.save()
        print(user.comment)
        return JsonResponse({'id':post_id, 'text':comment, 'comment_id':new_comment.id})
    

@login_required
@csrf_exempt
def change_like(request):
    if request.method=="POST":
        req=json.loads(request.body)
        post_id=req['id']
        updown=req['num']
        
        user=request.user
        post=Post.objects.get(id=post_id)
        
        if updown==1:
            post.like_users.add(request.user)
            post.likes+=1
        else:
            post.likes-=1
            post.like_users.remove(request.user)
        post.save()
        return JsonResponse({'id':post_id, 'num':post.likes})
    
@login_required
@csrf_exempt
def delete_comment(request):
    if request.method=="POST":
        req=json.loads(request.body)
        post_id=req['pid']
        comment_id=req['cid']
        comment=Comment.objects.get(id=comment_id)
        comment.delete()
        return JsonResponse({'id':post_id})