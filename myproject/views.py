#from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
#   return HttpResponse("hello this is root")
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
#return HttpResponse("this is about my life")