# from django.shortcuts import render
# from django.shortcuts import render, redirect  
# from django.http import HttpResponseRedirect, HttpResponse
# # Create your views here.
# def list(r):   
#     return HttpResponse ('Here are your students')  

# def insert(request):  
#     return render(request, 'insertstudent.html')  

# def update(request):    
#     return render(request, 'updatestudent.html') 

# def delete(r):   
#     return redirect("/student/list")  

# def index(request): #view for / 
#  return HttpResponseRedirect(“/posts”) 
 
# def get_posts(request): #view for /posts 
#  return HttpResponse (“Here are your posts”)


# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Student
# from .forms import StudentForm

# def student_list(request):
#     students = Student.objects.all()
#     return render(request, '../templates/studentlist.html', {'students': students})

# def student_detail(request, id):
#     student = get_object_or_404(Student, id=id)
#     return render(request, 'studentdetail.html', {'student': student})

# def student_create(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             student = form.save()
#             return redirect('student_detail', id=student.id)
#     else:
#         form = StudentForm()
#     return render(request, 'studentform.html', {'form': form})

# def student_update(request, id):
#     student = get_object_or_404(Student, id=id)
#     if request.method == 'POST':
#         form = StudentForm(request.POST, instance=student)
#         if form.is_valid():
#             student = form.save()
#             return redirect('student_detail', id=student.id)
#     else:
#         form = StudentForm(instance=student)
#     return render(request, 'studentform.html', {'form': form})

# def student_delete(request, id):
#     student = get_object_or_404(Student, id=id)
#     student.delete()
#     return redirect('student_list')
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student
from staff.models import Staff

def all_std(req):
    students = Student.objects.all()
    return render(req, 'student/std_list.html', {'students': students})

def insert(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        city = req.POST.get('city')
        supervisor_id = req.POST.get('supervisor')
        supervisor = Staff.objects.get(id=supervisor_id)
        student = Student(name=name, age=age, city=city, supervisor=supervisor)
        student.save()
        return redirect('/student/')
    supervisors = Staff.objects.all()
    return render(req, 'student/std_insert.html',{'supervisors': supervisors})

def update(req,std_id):
    student = get_object_or_404(Student, id=std_id)
    if req.method == 'POST':
        name = req.POST.get('name')
        age = req.POST.get('age')
        city = req.POST.get('city')
        supervisor_id = req.POST.get('supervisor')
        supervisor = Staff.objects.get(id=supervisor_id)
        student.name = name
        student.age = age
        student.city = city
        student.supervisor = supervisor
        student.save()
        return redirect('/student/')

    supervisors = Staff.objects.all()
    return render(req, 'student/std_update.html', {'student': student, 'supervisors': supervisors})



def delete(req,std_id):
    student = get_object_or_404(Student, id=std_id)
    student.delete()
    return redirect('/student/')
