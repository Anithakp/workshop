from django.http import HttpResponse
from django.shortcuts import render
from . models import destination
# Create your views here.
def home(request):
    #return HttpResponse("helloworld")
   # return render(request,'home.html')
    obj=destination.objects.all()
    return render (request,"index.html",{'keyobject':obj})