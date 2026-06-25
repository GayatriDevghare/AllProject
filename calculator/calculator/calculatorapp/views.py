from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, "home.html")

def Greet(request):
    return HttpResponse ("Good MOrning ")

def GetAdditionPage(request):
    return render(request,"Addition.html")

def GetSubtractionPage(request):
    return render(request,"Subtraction.html")

def GetMultiplicationPage(request):
    return render(request,"Multiplication.html")

def GetDivisionPage(request):
    return render(request,"Division.html")

def GetHomePage(request):
    return render(request,"Home.html")


def Addition(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]

    add = int(num1) + int(num2)

    return render (request,"Addition.html", {"num1":num1,"num2":num2, "ans":add, "msg":"Addition operation done !!!"})


def Subtraction(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]

    sub = int(num1) - int(num2)

    return render (request,"Subtraction.html", {"num1":num1,"num2":num2, "ans":sub, "msg":"Subtraction operation done !!!"})


def Multiplication(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]

    mul = int(num1) * int(num2)

    return render (request,"Multiplication.html", {"num1":num1,"num2":num2, "ans":mul, "msg":"Multiplication operation done !!!"})

def Division(request):
    num1 = request.GET["num1"]
    num2 = request.GET["num2"]

    div = int(num1) / int(num2)

    return render (request,"Division.html", {"num1":num1,"num2":num2, "ans":div, "msg":"Division operation done !!!"})

def HomePage(request):
    return render(request,"Home.html")