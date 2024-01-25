from django.shortcuts import render
from django.http import HttpResponse

def salomlash(request):
    return HttpResponse("<h1>Salom, Dunyo!</h1>")
def bosh_sahifa(request):
    return render(request,"hi.html")
def ob_havo(request):
    return render(request,"ob.html")

import .models import *
def hamma_kitoblar(request):
    data = {
        "books":Kitob.objects.all()
    }
    return render(request,"kitoblar.html",data)