from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

#function based views
# it accepts request from browser and return http response
def display(request):
    return HttpResponse("<h1>My First Django APP!!!</h1>")

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = "<b>Current Date and Time:</b>"+str(dt)
    return HttpResponse(s);
#class based views
