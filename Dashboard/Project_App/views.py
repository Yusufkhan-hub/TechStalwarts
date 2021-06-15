from django.shortcuts import render
from .forms import UserForms
from .models import User
from django.contrib import messages
# Create your views here.


def get_user(request):
    obj  = User.objects.all()
    return render(request,'home.html',{'obj':obj})


def post_user(request):
    form = UserForms()
    if request.method=='POST':
        form = UserForms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Data added successfully")
            return render(request,'post-data.html')
        else:
            messages.error(request,"Something went try again")
            return render(request,"post-data.html")
    else:
        form = UserForms()
    return render(request,"post-data.html",{'form':form}) 