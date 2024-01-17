from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from .forms import IdeaForm
from .models import *
# Create your views here.
def main(request):
    sort = request.GET.get('sort','')
    if sort == 'title':
        ideas = Idea.objects.all().order_by('title')
    elif sort ==  'olddate':
        ideas = Idea.objects.all().order_by('created_date')
    elif sort == 'newdate':
        ideas = Idea.objects.all().order_by('-created_date')
    else:
        ideas = Idea.objects.all().order_by('-interest')
    ctx={'ideas':ideas}
    return render(request, "ideas/idea_list.html", ctx)

def create(request):
    if request.method=="POST":
        form=IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea_now=form.save()
            ideastar=IdeaStar.objects.create(idea=idea_now)
            
            
        return redirect('ideas:main')
    
    form=IdeaForm()
    ctx={'form':form}
    return render(request, "ideas/idea_create.html", ctx)

def detail(request,pk):
    idea=Idea.objects.get(id=pk)
    ctx={'idea':idea,
         'pk':pk
         }
    return render(request, "ideas/idea_detail.html",ctx)

def update(request, pk):
    idea=Idea.objects.get(id=pk)
    if request.method=="POST":
        form=IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
        return redirect("ideas:detail",pk)
    
    form=IdeaForm(instance=idea)
    ctx={'form':form,
         'pk':pk
         }    
    return render(request, 'ideas/idea_update.html', ctx)

def delete(request,pk):
    if request.method=="POST":
        idea=Idea.objects.get(id=pk)
        print(idea)
        idea.delete()
    return redirect('ideas:main')

def change_interest(request):
    dic=request.POST.dict()
    idea=Idea.objects.get(id=dic['field1'])
    idea.interest+=int(dic['field2'])
    print(idea.interest)
    idea.save()   
#     print(idea_id, value)
#     idea = get_object_or_404(Idea, pk=idea_id)
#     idea.interest += value
#     idea.save()
    return JsonResponse({'interest': idea.interest})

def change_heart(request):
    dic=request.POST.dict()
    idea=Idea.objects.get(id=dic['id'])
    ideastar=idea.ideastar
    print(dic['heart'])
    if dic['heart']=="True":
        print("here")
        ideastar.star=True
    else:
        ideastar.star=False
    print(ideastar)
    ideastar.save()
    return JsonResponse({'interest': idea.interest})
    
def update_interest_level(request):
    interest_level = request.POST.get('interestLevel')
    # Do something with the interest level
    
    return JsonResponse({'success': True})
    