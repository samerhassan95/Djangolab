from django.shortcuts import render
from django.shortcuts import render, redirect  
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
def liststudents(r):   
    return redirect("/student/list")  

def liststaff(request):  
    return redirect("/staff/list")  

def mainreport(request):    
    return render(request, 'report.html') 

