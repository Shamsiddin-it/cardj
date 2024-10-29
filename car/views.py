from django.shortcuts import render,redirect
from .models import *
from .forms import CarForm, CompanyForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")

def cars(request):
    cars = Car.objects.all()
    return render(request, "cars.html", {"cars": cars})

def get_car(request, pk):
    car = Car.objects.filter(id = pk).first()
    return render(request, "get_car.html", {"car":car})

def get_company(request, pk):
    company = Company.objects.filter(id = pk).first()
    return render(request, "get_company.html", {"company":company})

def companies(request):
    companies = Company.objects.all()
    return render(request, "companies.html", {"companies": companies})

def add_car(request):
    form = CarForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("cars")
    else:
        form = CarForm()
    return render(request, "add_car.html", {"form":form})

def add_company(request):
    form = CompanyForm(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("companies")
    else:
        form = CompanyForm()
    return render(request, "add_company.html", {"form":form})

def update_car(request, pk):
    car = Car.objects.filter(id = pk).first()
    if car:
        form = CarForm(request.POST, request.FILES, instance=car)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("cars")
        else:
            form = CarForm(instance=car)
        return render(request, "update_car.html", {"form":form})
    else:
        return HttpResponse("not found")

def update_company(request, pk):
    company = Company.objects.filter(id = pk).first()
    if company:
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect("companies")
        else:
            form = CompanyForm(instance=company)
        return render(request, "update_company.html", {"form":form})
    else:
        return HttpResponse("not found")
    
def delete_car(request, pk):
    car = Car.objects.filter(id = pk).first()
    if car:
        if request.method == "POST":
                car.delete()
                return redirect("cars")
        return render(request, "delete_car.html", {"car":car})
    else:
        return HttpResponse("not found")

def delete_company(request, pk):
    company = Company.objects.filter(id = pk).first()
    if company:
        if request.method == "POST":
                company.delete()
                return redirect("companies")
        return render(request, "delete_company.html", {"company":company})
    else:
        return HttpResponse("not found")