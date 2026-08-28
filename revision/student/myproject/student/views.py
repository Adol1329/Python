from django.shortcuts import render
from .models import Student
# Create your views here.
def homepage(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")
def student_list(request):
    students={'students':Student.objects.all()}
    return render(request, "student_list.html",students)


def contact(request):
    return render(request,"")