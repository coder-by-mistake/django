from django.shortcuts import render

# Create your views here.
from .models import blog, employee,company

def get_total_employees(self):
    return self.employee_set.count()

