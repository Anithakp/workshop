from django.http import HttpResponse
from django.shortcuts import render
from . models import destination,book
# Create your views here.
# def home(request):
#     #return HttpResponse("helloworld")
#    # return render(request,'home.html')
#     obj=destination.objects.all()
#     return render (request,"index.html",{'keyobject':obj})

def home(request):
    #return HttpResponse("helloworld")
   # return render(request,'home.html')
    obj=book.objects.all()
    return render (request,"add.html",{'book':obj})

def add_book(request) :
    if request.method == "POST":
        name= request.POST.get('name')
        desc= request.POST.get('desc')
        book_image = request.FILES['book_image']
        bk=book(name=name,desc=desc,image=book_image)
        bk.save()
    return render(request,"add_book.html")
