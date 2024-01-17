from django.shortcuts import render,redirect
from .models import Devtool
from .forms import DevtoolForm

# Create your views here.
def main(request):
    devtools=Devtool.objects.all()
    return render(request, "devtools/devtool_list.html", {'devtools':devtools} )

def create(request):
    print(request)
    if request.method=="POST":
        form=DevtoolForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('devtools:main')
    
    form=DevtoolForm()
    ctx={'form':form}
    return render(request, "devtools/devtool_create.html", ctx)


def detail(request,pk):
    devtool=Devtool.objects.get(id=pk)
    related_ideas=devtool.idea_set.all()
    ctx={'devtool':devtool,
         'pk':pk,
         'related_ideas':related_ideas
         }
    return render(request, "devtools/devtool_detail.html",ctx)

def update(request, pk):
    devtool=Devtool.objects.get(id=pk)
    if request.method=="POST":
        form=DevtoolForm(request.POST, instance=devtool)
        if form.is_valid():
            form.save()
        return redirect("devtools:detail",pk)
    
    form=DevtoolForm(instance=devtool)
    ctx={'form':form,
         'pk':pk
         }    
    return render(request, 'devtools/devtool_update.html', ctx)

def delete(request,pk):
    if request.method=="POST":
        Devtool.objects.get(id=pk).delete()
    return redirect('devtools:main')
    
    