from django.shortcuts import render,redirect
from .models import kelvin,Tag
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import ProjectForm
from django.db.models import Q


def add(resquest):
    search_project_query=''
    
    if resquest.GET.get("search_project_query"):
        search_project_query=resquest.GET.get("search_project_query")
        
    tags=Tag.objects.filter(name__icontains=search_project_query)
    
    
    value=kelvin.objects.distinct().filter(Q(title__icontains=search_project_query)|
                                           Q(Tags__in=tags))
    
    paginator = Paginator(value,1)
    page_number = resquest.GET.get('page')
    page_obj = paginator.get_page(page_number)
    content={"projects":page_obj,"search_project_query":search_project_query}
    return render(resquest,'abc/main.html',content)

def abc(resquest,a):
    projectid=kelvin.objects.get(id=a)
    Tb=projectid.Tags.all()
    projectsid={"pid":projectid,'Tags':Tb}
    return render(resquest,"abc/single_project.html",projectsid)

@login_required(login_url='login')
def createProject(resquest):
    form=ProjectForm()
    if resquest.method=='POST':
        # print(resquest.POST)
        form=ProjectForm(resquest.POST,resquest.FILES)
        if form.is_valid():
            form.save()
            return redirect('add')
    return render(resquest,"abc/addproject.html",{"form":form})

@login_required(login_url='login')
def updateProject(resquest,up):
    updatep=kelvin.objects.get(id=up)
    form=ProjectForm(instance=updatep)
    if resquest.method=='POST':
        # print(resquest.POST)
        form=ProjectForm(resquest.POST,resquest.FILES,instance=updatep)
        if form.is_valid():
            form.save()
            return redirect('add')
    return render(resquest,"abc/addproject.html",{"form":form})

@login_required(login_url='login')
def deleteProject(resquest,dp):
    deleteP=kelvin.objects.get(id=dp)
    if resquest.method=="POST":
        deleteP.delete()
        return redirect('add')
    return render(resquest,"abc/deleteProject.html",{"context":deleteP})