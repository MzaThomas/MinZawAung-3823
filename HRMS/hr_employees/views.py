from django.shortcuts import render, redirect
from .models import EmployeeModel
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.core.paginator import Paginator
from hr_tags.models import EmployeeTagModel
from hr_jobs.models import JobModel
from django.contrib import messages

def search_by(request):
    search = request.GET.get('search')
    if search:    
        employees = EmployeeModel.objects.filter(
            Q(name__icontains=search) | 
            Q(age__icontains=search) |
            Q(birthday__icontains=search) |
            Q(address__icontains=search) |
            Q(email__icontains=search) |
            Q(gender__icontains=search) |
            Q(joining_date__icontains=search)
        )
    else:      
        employees = EmployeeModel.objects.all()
    return render(request, 'employee_list.html', {'page_obj': employees})

def order_by(request):
    print('order by call')
    order = request.GET.get('order')
    employees = EmployeeModel.objects.all().order_by("-" + order)
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(employees, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'employee_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

def logout_view(request):
    logout(request)
    return redirect('/login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            return redirect('/hr_employees/show_employee/')
        else:
            messages.error(request, "Incorrect Username and / or Password.")
            return render(request, 'login.html')
            # return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        return render(request, 'login.html')

@permission_required('hr_employees.view_employeemodel', login_url='login')
def employee(request, employee_id):
    if request.method == "GET":
        employee = EmployeeModel.objects.get(id=employee_id)
        context = {'employee': employee}
        return render(request,'employee_detail.html', context)

@login_required(login_url='login')
def all_employees(request):
    if request.method == "GET":
        all_employees = EmployeeModel.objects.all()
        paginator = Paginator(all_employees, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'employee_list.html', {'page_obj': page_obj})

@permission_required('hr_employees.add_employeemodel', login_url='login')
def add_employee(request):  
    if request.method == "GET":
        employee = EmployeeModel()
        jobs = JobModel.objects.all()
        tags = EmployeeTagModel.objects.all()
        return render(request,'employee_create.html',{'employee': employee, 'jobs': jobs, 'tags': tags})
    if request.method == "POST" and request.FILES['image']:
        name = request.POST.get('name')
        age = request.POST.get('age')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gender = request.POST.get('gender')
        if request.POST.get('is_married') == 'on':
           is_married = True
        else:
           is_married = False
        job = request.POST.get('job')
        tags = request.POST.getlist('tags')
        joining_date = request.POST.get('joining_date')
        tenure = request.POST.get('tenure')
        image = request.FILES.get('image')
        employee = EmployeeModel.objects.create(
            name=name, 
            age=age, 
            birthday=birthday,
            address=address,
            email=email,
            phone_number=phone_number,
            gender=gender,
            job_id=job,
            is_married=is_married,
            joining_date=joining_date,
            tenure=tenure,
            image=image
        )
        employee.tags.set(tags)
        employee.save()
        messages.success(request, 'Form saved successfully.')
        return redirect('/hr_employees/show_employee/')

@permission_required('hr_employees.change_employeemodel', login_url='login')
def update_employee(request, employee_id):  
    employee = EmployeeModel.objects.get(id=employee_id)  
    if request.method == "GET":
        employee.birthday = str(employee.birthday)
        jobs = JobModel.objects.all()
        tags = EmployeeTagModel.objects.all()
        employee.joining_date = datetime.strftime(employee.joining_date, '%Y-%m-%dT%H:%M')
        context = {'employee': employee, 'uploaded_image': employee.image, 'jobs': jobs, 'tags': tags}
        return render(request, 'employee_update.html', context)
    elif request.method == "POST": 
        employee.name = request.POST.get('name')
        employee.age = request.POST.get('age')
        employee.birthday = request.POST.get('birthday')
        employee.address = request.POST.get('address')
        employee.email = request.POST.get('email')
        employee.phone_number = request.POST.get('phone_number')
        employee.gender = request.POST.get('gender')
        if request.POST.get('is_married') == 'on':
           employee.is_married = True
        else:
           employee.is_married = False
        #employee.is_married = request.POST.get('is_married')
        employee.joining_date = request.POST.get('joining_date')
        employee.tenure = request.POST.get('tenure')
        if request.FILES.get('image'):
            employee.image = request.FILES.get('image')
        employee.job_id = request.POST.get('job')
        employee.tags.set(request.POST.getlist('tags'))
        employee.save()
        messages.success(request, 'Form updated successfully.')
        return redirect('/hr_employees/detail/' + str(employee_id) + '/')

@permission_required('hr_employees.delete_employeemodel', login_url='login')
def delete_employee(request, employee_id):
    if request.method == "GET":
        employee = EmployeeModel.objects.get(id=employee_id)
        employee.delete()
        messages.success(request, 'Form deleted successfully.')
        return redirect('/hr_employees/show_employee/')
