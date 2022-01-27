from django.shortcuts import render
from .forms import RequestForm

def home(request):
    return render(request,'main/index.html')

def approach(request):
    return render(request,'main/approach.html')

def web_development(request):
    return render(request,'main/web_development.html')