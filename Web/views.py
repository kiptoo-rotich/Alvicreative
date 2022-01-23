from django.shortcuts import render
from .forms import RequestForm

def home(request):
    form = "Wei"
    return render(request,'main/index.html',{'form':form})