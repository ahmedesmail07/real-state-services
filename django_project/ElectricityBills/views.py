from django.shortcuts import render, HttpResponse

from .models import  PaymentForm, MeterRequestForm,PayBillsForm,LicenseRequestForm,ReconciliationRequestForm
# Create your views here.


def provideElectricMeter(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ElectricityBills/form1.html')
        else:
            form = PaymentForm()
        return render(request, 'ElectricityBills/form1.html', {'form': form,
                                                               })
    else:
        form = PaymentForm()
    return render(request, 'ElectricityBills/form1.html', {'form': form,
                                                           })


def form2(request):
    if request.method == 'POST':
        form = MeterRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ElectricityBills/form2.html')
        else:
            form = MeterRequestForm()
        return render(request, 'ElectricityBills/form2.html', {'form': form,
                                                               })
    else:
        form = MeterRequestForm()
        return render(request, 'ElectricityBills/form2.html')

def form3(request):
    if request.method == 'POST':
        form = PayBillsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'ElectricityBills/form3.html')
        else:
            form = PayBillsForm()
        return render(request, 'ElectricityBills/form3.html', {'form': form,
                                                               })
    else:
        form = PayBillsForm()
        return render(request, 'ElectricityBills/form3.html')

def form4(request):
    if request.method == 'POST':
        form = LicenseRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'ElectricityBills/form4.html')
        else:
            print(form.errors)
            return render(request,'ElectricityBills/form4.html')

    else:
        form = LicenseRequestForm()
        return render(request, 'ElectricityBills/form4.html')

def form5(request):
    if request.method == 'POST':
        form = ReconciliationRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'ElectricityBills/form5.html')
        else:
            print(form.errors)
            return render(request,'ElectricityBills/form5.html')

    else:
        form = ReconciliationRequestForm()
        return render(request, 'ElectricityBills/form5.html')