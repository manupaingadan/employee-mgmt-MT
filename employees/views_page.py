# employees/views_page.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_page(request):
    return render(request, "employees/login.html")

def formbuilder_page(request):
    return render(request, "employees/formbuilder.html")

def employee_create_page(request):
    return render(request, "employees/employee_create.html")

def employee_list_page(request):
    return render(request, "employees/employee_list.html")
