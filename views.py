from django.shortcuts import render
from django.http import HttpResponse
from . models import Portfolio

# Create your views here.
def home(request):
    portfolios = Portfolio.objects.all()
    return render(request,'index.html', {'portfolio': portfolios})
    # return HttpResponse("hiii")