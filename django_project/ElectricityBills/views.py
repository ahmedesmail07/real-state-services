from django.shortcuts import render

# Create your views here.
def test(request):
    codenumber = request.POST.get("number")
    meterreding = request.POST.get("meterreder")
    company = request.POST.get("address")
    image = request.POST.get("image")
    comments = request.POST.get("comment")
    return render(request,'ElectricityBills/form1.html')