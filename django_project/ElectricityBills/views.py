from django.shortcuts import render,HttpResponse

from .models import Payment,PaymentForm
# Create your views here.
def provideElectricMeter(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'ElectricityBills/form1.html')
    else:
        form = PaymentForm()
    return render(request, 'ElectricityBills/form1.html', {'form': form,
                                                           'error_msg':'You entered wrong data'})
def form2(request):
    return render(request, 'ElectricityBills/form2.html')
