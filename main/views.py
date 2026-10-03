from django.shortcuts import render

from .models import Student


def home(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "main/home.html", context)
