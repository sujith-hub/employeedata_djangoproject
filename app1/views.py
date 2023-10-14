from django.shortcuts import render
from django.shortcuts import redirect
from .models import employee
# Create your views here.

def employeedata(request):
    if request.method=='GET':
        return render(request,'employee.html')
    else:
        employee(
            firstname=request.POST.get('firstname'),
            lastname=request.POST.get('lastname'),
            employeeid=request.POST.get('employeeid'),
            mobile=request.POST.get('mobile'),
            dateofbirth=request.POST.get('dob'),
            experience=request.POST.get('experience'),
            salary=request.POST.get('salary'),
        ).save()
        return render(request,'employee.html')
