from django.shortcuts import render
from .forms import LogForm
# Create your views here.
def viewForm(request):
    form = LogForm()
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request,'form.html',context)
    