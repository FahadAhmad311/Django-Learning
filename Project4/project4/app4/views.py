from django.shortcuts import render
from .forms import LogCollege
from .forms import LogPrincipal
from .forms import LogSubject
from .forms import LogTeacher

# Create your views here.
def viewCollege(request):
    form = LogCollege()
    if request.method == "POST":
        form = LogCollege(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, 'college.html',context)        

def viewPrincipal(request):
    form = LogPrincipal()
    if request.method == "POST":
        form = LogPrincipal(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, 'principal.html',context)        

def viewSubject(request):
    form = LogSubject()
    if request.method == "POST":
        form = LogSubject(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, 'subject.html',context) 

def viewTeacher(request):
    form = LogTeacher()
    if request.method == "POST":
        form = LogTeacher(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, 'teacher.html',context)               