from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.
def index(request):
    if request.method=="POST":
     
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        employee=Employee( name=name, email=email,password=password)
        employee.save()
    emps=Employee.objects.all()
    return render(request,'index.html',{'empl':emps})

def delete_emp(request,emp_id):
    emp=Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect('index')

def update_emp(request,emp_id):
    data=Employee.objects.get(pk=emp_id)

    return render(request,'update.html',{'data':data})

def do_update_emp(request, emp_id):
    # if request.method=="POST":
   
     name=request.POST.get('name')
     email=request.POST.get('email')
     password=request.POST.get('password')
     data=Employee.objects.get(pk=emp_id)
    #  data=Employee(name=name, email=email, password=password)
     data.name=name
     data.email=email
     data.password=password
    #  worker=Employee( name=name, email=email,password=password)
     data.save()
     return redirect('index')
