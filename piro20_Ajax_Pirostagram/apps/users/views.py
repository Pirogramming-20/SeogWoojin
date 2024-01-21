from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.
def main(request):
    return redirect('posts:main')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('users:main')
        else:
            ctx={
                'form':form,
            }
            return render(request, 'users/signup.html',context=ctx) # 이부분 수정
    else:
        form = SignupForm()
        context={
            'form': form,
        }
        return render(request, template_name='users/signup.html', context=context)
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('users:main')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name='users/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='users/login.html', context=context)
    
    
def logout(request):
    auth.logout(request)
    return redirect('posts:main')