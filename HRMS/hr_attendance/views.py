from django.shortcuts import render, redirect
from .models import AttendanceModel
from .forms import AttendanceForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.

def search_by(request):
    search = request.GET.get('search')
    if search:    
        attendance = AttendanceModel.objects.filter(
            Q(name__icontains=search) |
            Q(date__icontains=search)
        )
    else:      
        attendance = AttendanceModel.objects.all()
    return render(request, 'attendance_list.html', {'page_obj': attendance})

def order_by(request):
    order = request.GET.get('order')
    attendance = AttendanceModel.objects.all().order_by("-"+ order)
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(attendance, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'attendance_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

@login_required(login_url='login')
def all_attendances(request):
    if request.method == "GET":
        all_attendances = AttendanceModel.objects.all()
        paginator = Paginator(all_attendances, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'attendance_list.html', {'page_obj': page_obj})

@permission_required('hr_attendance.view_attendancemodel', login_url='login')
def attendance(request, attendance_id):
    if request.method == "GET":
        attendance = AttendanceModel.objects.get(id=attendance_id)
        return render(request,'attendance_detail.html', {'attendance': attendance})

@permission_required('hr_attendance.add_attendancemodel', login_url='login')
def add_attendance(request):
    if request.method == "GET":
        form = AttendanceForm()
        return render(request,'attendance_create.html',{'form':form})
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            employee = form.cleaned_data.get('employee')
            job = form.cleaned_data.get('job')
            department = form.cleaned_data.get('department')
            date = form.cleaned_data.get('date')
            tags = form.cleaned_data.get('tags')
            attendance = AttendanceModel.objects.create(
                name=name,
                employee=employee,
                job=job,
                department=department,
                date=date
            )
            attendance.tags.set(tags)
            attendance.save()
            messages.success(request, 'Form saved successfully.')
            return redirect('/hr_attendance/show_attendance/')

@permission_required('hr_attendance.change_attendancemodel', login_url='login')
def update_attendance(request, attendance_id):
    attendance = AttendanceModel.objects.get(id=attendance_id)
    if request.method == "GET":
        values = {
            'name': attendance.name,
            'employee': attendance.employee,
            'job': attendance.job,
            'department': attendance.department,
            'date': attendance.date,
            'tags': attendance.tags.all()
        }
        form = AttendanceForm(initial=values)
        context = {'form': form, 'attendance': attendance}
        return render(request, 'attendance_update.html', context)
    elif request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance.name = form.cleaned_data.get('name')
            attendance.employee = form.cleaned_data.get('employee')
            attendance.job = form.cleaned_data.get('job')
            attendance.department = form.cleaned_data.get('department')
            attendance.date = form.cleaned_data.get('date')
            attendance.tags.set(form.cleaned_data.get('tags'))
            attendance.save()
            messages.success(request, 'Form updated successfully.')
            return redirect('/hr_attendance/detail/' + str(attendance_id) + '/')

@permission_required('hr_attendance.delete_attendancemodel', login_url='login')
def delete_attendance(request, attendance_id):
    if request.method == "GET":
        attendance = AttendanceModel.objects.get(id=attendance_id)
        attendance = AttendanceModel.objects.filter(id=attendance_id)
        attendance.delete()
        messages.success(request, 'Form deleted successfully.')
        return redirect('/hr_attendance/show_attendance/')