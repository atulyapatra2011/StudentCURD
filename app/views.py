from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from .forms import StudentForm
from .models import Student
from django.urls import reverse
from xhtml2pdf import pisa
from io import BytesIO
# from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def Dasgboard(request):
    return render(request, 'Dashboard.html')

def Home(request):
    return render(request, 'Home.html')

def Add_Student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your was successful! Added in Database')
            return render(request, 'Add_Student.html', {'form': StudentForm(), 'success': True})
        else:
            messages.error(request,'Your action was getting wrong !! please check it')
            return render(request, 'Add_Student.html', {'form': form, 'error': True})
    else:
        form = StudentForm()
    return render(request, 'Add_Student.html', {'form': form})

def Student_List(request):
    student = Student.objects.all()
    paginator  = Paginator(student,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    dict = {'page_obj':page_obj}
    return render(request, 'Student_List.html', dict)

def Edit_Student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your was successful! Edited in Database')
            return redirect(reverse('student_list'))
        else:
            messages.error(request,'Your action was getting wrong !! please check it')
            return render(request, 'Edit_Student.html', {'form': form, 'error': True})
    return render(request, 'Edit_Student.html', {'form': StudentForm(instance=student)})

def Delete_Student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, 'Your was successful! Deleted value')
    return redirect(reverse('student_list'))

def pdf_Student(request, id):
    student = get_object_or_404(Student,id=id)
    # print(student)
    logo_url = request.build_absolute_uri(student.profile_picture.url)
    html = render(request,'student_id_details.html',{'student':student,'logo_url': logo_url})


    

    # Generate PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="student_{id}.pdf"'

    pisa_status = pisa.CreatePDF(
        src=html.content.decode('utf-8'),
        dest=response
    )

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response
    
def pdf_table(request):
    student = Student.objects.all()
    # logo_url = request.build_absolute_uri(student.profile_picture.url)
    html =  render(request,'student_all_details.html',{'student':student})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="student_all_{id}.pdf"'

    pisa_status = pisa.CreatePDF(
        src=html.content.decode('utf-8'),
        dest=response
    )

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response
