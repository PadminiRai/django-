# Create your views here.
from django.shortcuts import render,redirect
from .forms import *
from .models import *
def employee_list(request):
    # employeel = list()
    employeel = list(Employee.objects.values('eno', 'ename', 'mobile', 'position_id'))
    # for i in range(len(Employee.objects.all())):
    #     print("i")
    #     employeel.append(employeeobj[i])
    context = {'employeel':employeel}
    print(len(context['employeel']))
    print(context)
    return render(request,"employee_register/employee_list.html",context)
def employee_form(request):
    
    if request.method == "GET":
        form = EmployeeForm()
        return render(request,"employee_register/employee_form.html",{'form':form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/employee/list/")

def employee_delete(request):
    return render(request,"employee_list.html")

def safety_ohs_a9(request, *args, **kwargs):
 context={}
 return render(request,'employee_register/safety_ohs_sec_a_9.html',context)

def homepagef(request, *args, **kwargs):
 context={}
 return render(request,'employee_register/homepage.html',context)

def charityregisterf(request, *args, **kwargs):
 context={}
 b1 = request.GET.get('b1')
 b2 = request.GET.get('b2')
 if details.objects.filter(uid=b1).count()==0:
     print("not found")
 return render(request,'employee_register/charityregister.html',context)

def editschemef(request, *args, **kwargs):
 context={}
 return render(request,'employee_register/editscheme.html',context)

def acceptf(request, *args, **kwargs):
 context={}
 return render(request,'employee_register/accept.html',context)


