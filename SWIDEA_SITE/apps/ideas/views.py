from django.shortcuts import render,redirect
from django.http import JsonResponse
from .forms import IdeaForm
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        
    page = request.GET.get('page')
    print(sort,page)
    items_per_page = 4
    paginator = Paginator(ideas, items_per_page)
    try:
        # 현재 페이지에 해당하는 항목 가져오기
        items = paginator.page(page)
    except PageNotAnInteger:
        # 페이지 번호가 정수가 아닌 경우, 첫 번째 페이지로 설정
        items = paginator.page(1)
    except EmptyPage:
        # 페이지가 비어 있는 경우, 마지막 페이지로 설정
        items = paginator.page(paginator.num_pages)    
    print(sort)
    ctx={'ideas':items,
         'order_by_field': sort}
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
    
    