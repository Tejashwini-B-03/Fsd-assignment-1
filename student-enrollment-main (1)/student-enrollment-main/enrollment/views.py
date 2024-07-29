from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import StudentForm
from .models import Student
import csv
from django.template.loader import get_template
from xhtml2pdf import pisa

def home(request):
    form = StudentForm()
    return render(request, 'enrollment/home.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Student registered successfully'})
    return JsonResponse({'errors': form.errors})

def generate_csv(request):
    students = Student.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Enrolled Date'])

    for student in students:
        writer.writerow([student.first_name, student.last_name, student.email, student.enrolled_date])

    return response

def generate_pdf(request):
    students = Student.objects.all()
    template_path = 'enrollment/students_pdf.html'
    context = {'students': students}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="students.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
