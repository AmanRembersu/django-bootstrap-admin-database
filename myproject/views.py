from django.shortcuts import render,HttpResponse
from datetime import datetime 
from myapp.models import Contact
from django.contrib import messages
def index(request):
    context={
        'var':"variable",
        'var1':"variable 2"
    }
    
    return render(request,'index.html',context)
#context is a set of variables whish is sent

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("service")

def contact(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact = Contact(name=name,email=email,message=message,date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent")
    
    return render(request,'contact.html')
    #return HttpResponse("contact")
    
