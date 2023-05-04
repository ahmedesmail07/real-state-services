from django.shortcuts import render,HttpResponse

from .models import Payment,PaymentForm,MeterRequest,MeterRequestForm
# Create your views here.
def provideElectricMeter(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ElectricityBills/form1.html')
    else:
        form = PaymentForm()
    return render(request, 'ElectricityBills/form1.html', {'form': form,
                                                           'error_msg':'You entered wrong data'})


def form2(request):
    if request.method == 'POST':
        form = MeterRequestForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'ElectricityBills/form2.html')
    else:
        form = MeterRequestForm()
    return render(request, 'ElectricityBills/form2.html', {'form': form,
                                                           'error_msg':'You entered wrong data'})
