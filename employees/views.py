from django.http import Http404
from django.shortcuts import get_object_or_404, render
from employees.models import Employee

def employee_detail(request, pk):
  employee = get_object_or_404(Employee, pk=pk)
  context = {
    'first_name': employee.first_name,
    'last_name': employee.last_name,
    'photo': employee.photo,
    'designation': employee.designation,
    'email_address': employee.email_address,
    'phone_number': employee.phone_number,
    'created_at': employee.created_at,
    'updated_at': employee.updated_at,
  }
  return render(request, 'employee_detail.html', context)
