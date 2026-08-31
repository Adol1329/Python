from django.shortcuts import render

from .models import Student
from .forms import ContactForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentSerializer

def homepage(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def student_list(request):
    students = {
        "students": Student.objects.all()
    }
    return render(request, "student_list.html", students)


def contact(request):

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

@api_view(["GET", "POST"])
def student_api(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
