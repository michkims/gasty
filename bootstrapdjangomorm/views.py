import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    now = datetime.datetime.now()
    html = "<html><body><h2>Now time is %s.</h2></body></html>" % now
    return HttpResponse(html)
def Home(request):
    return render(request,'home.html')
def Aboutus(request):
    return render(request, 'aboutus.html')
def Services(request):
    return render(request, 'services.html')
def Portfolio(request):
    return render(request, 'portfolio.html')
def Contactus(request):
    return render(request, 'contactus.html')
def Index(request):
    return render(request, 'index.html')


