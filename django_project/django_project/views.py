from django.shortcuts import render
def service(request):
    return render(request,'services.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')