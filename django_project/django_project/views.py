from django.shortcuts import render
from ElectricityBills.models import MeterRequest,PayBills,Payment

def services(request):
    return render(request, 'services.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
#all dashboard funcitons here 
def dashboard(request):
    return render(request,'Dashboard/project.html')

def electricityServices(request):
    return render(request,'Dashboard/electric.html')

def dashelec1(request):
    meter_requests = MeterRequest.objects.all()
    context = {'meter_requests': meter_requests}
    return render(request, 'Dashboard/dashelec1.html', context)

def dashelec2(request):
        pay_bills = PayBills.objects.all()
        context = {'pay_bills': pay_bills}
        return render(request,'Dashboard/dashelec2.html',context)

def dashelec3(request):
        payment = Payment.objects.all()
        context = {'payment': payment}
        return render(request,'Dashboard/dashelec3.html',context)
