from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db import connection

from .models import empinfo


# ==========================
# PAGE VIEWS
# ==========================

def GetBasePage(request):
    return render(request, 'base.html')


def GETHomePage(request):
    return render(request, 'home.html')


def GetRegisterpage(request):
    return render(request, 'registration.html')


def GetLoginpage(request):
    return render(request, 'login.html')


def GetLogoutpage(request):
    return render(request, 'login.html')


def GetEmployeecurdPage(request):
    return render(request, 'employeecurd.html')


def GETShowAllPage(request):
    emp = empinfo.objects.all()
    return render(request, 'showall.html', {'emp': emp})


# ==========================
# REGISTER
# ==========================

def RegisterEmployee(request):

    if request.method == "POST":

        employeename = request.POST.get('Employeename')
        password = request.POST.get('password')
        mobno = request.POST.get('mobno')
        employeeid = request.POST.get('Employeeid')

        empinfo.objects.create(
            employeeid=employeeid,
            employeename=employeename,
            password=password,
            mobno=mobno
        )

        return render(request, 'login.html')

    return render(request, 'registration.html')


# ==========================
# LOGIN
# ==========================

def LoginEmployee(request):

    if request.method == "POST":

        employeename = request.POST.get('Employeename')
        password = request.POST.get('password')

        try:
            emp = empinfo.objects.get(
                employeename=employeename,
                password=password
            )

            request.session['empid'] = emp.employeeid

            return render(request, 'home.html')

        except empinfo.DoesNotExist:

            return render(
                request,
                'login.html',
                {'msg': 'Invalid Username or Password'}
            )

    return render(request, 'login.html')


# ==========================
# LOGOUT
# ==========================

def LogoutEmployee(request):
    logout(request)
    return render(request, 'login.html')


# ==========================
# ADD EMPLOYEE
# ==========================

def ADD_Employee(request):

    if request.method == "POST":

        employeeid = request.POST.get('employeeid')
        employeename = request.POST.get('employeename')
        employeeemail = request.POST.get('employeeemail')
        password = request.POST.get('password')
        mobno = request.POST.get('mobno')
        department = request.POST.get('department')
        designation = request.POST.get('designation')
        salary = request.POST.get('salary')
        date_of_joining = request.POST.get('date_of_joining')

        if empinfo.objects.filter(employeeid=employeeid).exists():

            return render(
                request,
                'employeecurd.html',
                {'msg': f'Employee ID {employeeid} already exists'}
            )

        empinfo.objects.create(
            employeeid=employeeid,
            employeename=employeename,
            employeeemail=employeeemail,
            password=password,
            mobno=mobno,
            department=department,
            designation=designation,
            salary=salary,
            date_of_joining=date_of_joining
        )

        return render(
            request,
            'employeecurd.html',
            {'msg': 'Employee Added Successfully'}
        )

    return render(request, 'employeecurd.html')


# ==========================
# SHOW SINGLE EMPLOYEE
# ==========================

def Show_Single_Employee(request):

    employeeid = request.POST.get('employeeid')

    try:

        emp = empinfo.objects.get(employeeid=employeeid)

        print(connection.queries)

        return render(
            request,
            'employeecurd.html',
            {'emp': emp}
        )

    except empinfo.DoesNotExist:

        return render(
            request,
            'employeecurd.html',
            {'msg': 'Employee Not Found'}
        )


# ==========================
# UPDATE EMPLOYEE
# ==========================

def Update_Employee(request):

    employeeid = request.POST.get('employeeid')

    emp = empinfo.objects.filter(employeeid=employeeid)

    if emp.exists():

        emp.update(
            employeename=request.POST.get('employeename'),
            employeeemail=request.POST.get('employeeemail'),
            password=request.POST.get('password'),
            mobno=request.POST.get('mobno'),
            department=request.POST.get('department'),
            designation=request.POST.get('designation'),
            salary=request.POST.get('salary'),
            date_of_joining=request.POST.get('date_of_joining')
        )

        print(connection.queries)

        return render(
            request,
            'employeecurd.html',
            {'msg': 'Employee Updated Successfully'}
        )

    return render(
        request,
        'employeecurd.html',
        {'msg': 'Employee Not Found'}
    )


# ==========================
# DELETE EMPLOYEE
# ==========================

def Delete_Employee(request):

    employeeid = request.POST.get('employeeid')

    emp = empinfo.objects.filter(employeeid=employeeid)

    if emp.exists():

        emp.delete()

        return render(
            request,
            'employeecurd.html',
            {'msg': 'Employee Deleted Successfully'}
        )

    return render(
        request,
        'employeecurd.html',
        {'msg': 'Employee Not Found'}
    )


# ==========================
# SHOW ALL EMPLOYEES
# ==========================

def DeleteEmployeeShowAll(request):

    emp = empinfo.objects.all()

    return render(
        request,
        'showall.html',
        {'emp': emp}
    )