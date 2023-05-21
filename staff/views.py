from django.shortcuts import render
from django.shortcuts import render, redirect  
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Staff
# Create your views here.
# def home(request):
#     # logic for your view
#     return render(request, 'base.html')

# def list(r):   
#     return HttpResponse ('Here are your staff')  


# def insert(request):  
#     return render(request, 'insertstaff.html')  

# def update(request):    
#     return render(request, 'updatestaff.html') 

# def delete(r):   
#     return redirect("/staff/list") 


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Staff
# from .forms import StaffForm

# def staff_list(request):
#     staffs = Staff.objects.all()
#     return render(request, 'stafflist.html', {'staffs': staffs})

# def staff_detail(request, id):
#     staff = get_object_or_404(Staff, id=id)
#     return render(request, 'staffdetail.html', {'staff': staff})

# def staff_create(request):
#     if request.method == 'POST':
#         form = StaffForm(request.POST)
#         if form.is_valid():
#             staff = form.save()
#             return redirect('staff_detail', id=staff.id)
#     else:
#         form = StaffForm()
#     return render(request, 'staffform.html', {'form': form})

# def staff_update(request, id):
#     staff = get_object_or_404(Staff, id=id)
#     if request.method == 'POST':
#         form = StaffForm(request.POST, instance=staff)
#         if form.is_valid():
#             staff = form.save()
#             return redirect('staff_detail', id=staff.id)
#     else:
#         form = StaffForm(instance=staff)
#     return render(request, 'staffform.html', {'form': form})

# def staff_delete(request, id):
#     staff = get_object_or_404(Staff, id=id)
#     staff.delete()
#     return redirect('staff_list')

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             error_message = 'Invalid username or password.'
#     else:
#         error_message = ''
#     return render(request, 'login.html', {'error_message': error_message})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def logout(request):
#     logout(request)
#     return redirect('home')

def all_staff(req):
    sups = Staff.objects.all()
    return render(req, 'staff/staff_list.html', {'sups': sups})

def insert(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        sup = Staff(name=name)
        sup.save()
        return redirect('/staff/')
    return render(req, 'staff/staff_insert.html')

def update(req,sup_id):
    sup = get_object_or_404(Staff, id=sup_id)
    if req.method == 'POST':
        name = req.POST.get('name')
        sup.name = name
        sup.save()
        return redirect('/staff/')

    return render(req, 'staff/staff_update.html', {'sup': sup})



def delete(req,sup_id):
    sup = get_object_or_404(Staff, id=sup_id)
    sup.delete()
    return redirect('/staff/')