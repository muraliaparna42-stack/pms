import csv
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def home(request):
    students=Student.objects.all()
    return render(request,'home.html',{'students':students})

def export_csv(request):
    students=Student.objects.all()

    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="students.csv"'

    writer=csv.writer(response)
    writer.writerow(['Name','Email','Course'])

    for student in students:
        writer.writerow([student.name,student.email,student.course])
    return response