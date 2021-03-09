from django.shortcuts import render

def index(request):
    return render(request,'studys/index.html')
# Create your views here.

def studya(request):
    return render(request,'studys/studya.html')
    
def studyb(request):
    return render(request,'studys/studyb.html')
    
def paizas(request):
    return render(request,'studys/paizas.html')
    
def paizaa(request):
    return render(request,'studys/paizaa.html')
    
def paizab(request):
    return render(request,'studys/paizab.html')

def myinfo(request):
    return render(request,'studys/myinfo.html')