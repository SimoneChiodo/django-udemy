from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def home(request):
  employess = Employee.objects.all() # Prendo tutti i dati salvati
  context = {
    'employess': employess,
  }
  return render(request, "home.html", context)
