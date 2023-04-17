from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import calculator


def home(request):
    return render(request, 'index.html')

@login_required
def getDataPage(request):
    return render(request,'data.html')

@login_required
def logic(request):
    if request.method == 'POST':
        amount = int(request.POST["amount"])
        guests = int(request.POST["guests"])
        location = request.POST["city"]
        venue = request.POST["venue"]
        result = calculator.calculator(amount, location, guests, venue)
        if result == 'economic budget':
            return render(request, 'result.html', {'result':result, 'price':'₦500,000'})
        elif result == 'standard budget':
            return render(request, 'result.html', {'result':result, 'price':'₦1,000,000'})
        else:
            return render(request, 'result.html', {'result':result, 'price':'₦2,500,000'})

