from django.shortcuts import render

# Create your views here.
def login(req):
    return render(req,'access/login.html')

def reg(req):
    return render(req,'access/register.html')