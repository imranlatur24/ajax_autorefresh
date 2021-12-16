from django.shortcuts import render
from .models import StudentModel
from django.http import JsonResponse
# Create your views here.

def dashboard(request):
    return render(request,"index.html")

def student_data(request):
    stud = StudentModel.objects.all()
    return JsonResponse({'students':list(stud.values())})

