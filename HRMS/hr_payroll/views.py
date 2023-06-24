from django.shortcuts import render, redirect
from .models import PayrollModel
from .forms import PayrollForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

# Create your views here.

def search_by(request):
    search = request.GET.get('search')
    if search:    
        payroll = PayrollModel.objects.filter(
            Q(name__icontains=search) |
            Q(salary__icontains=search) |
            Q(pay_date__icontains=search)
        )
    else:      
        payroll = PayrollModel.objects.all()
    return render(request, 'payroll_list.html', {'page_obj': payroll})

def order_by(request):
    order = request.GET.get('order')
    payroll = PayrollModel.objects.all().order_by("-"+ order)
    order_selected = {str(order): 'btn-primary text-white'}
    paginator = Paginator(payroll, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'payroll_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

@login_required(login_url='login')
def all_payrolls(request):
    if request.method == "GET":
        all_payrolls = PayrollModel.objects.all()
        paginator = Paginator(all_payrolls, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'payroll_list.html', {'page_obj': page_obj})

@permission_required('hr_payroll.view_payrollmodel', login_url='login')
def payroll(request, payroll_id):
    if request.method == "GET":
        payroll = PayrollModel.objects.get(id=payroll_id)
        return render(request,'payroll_detail.html', {'payroll': payroll})

@permission_required('hr_payroll.add_payrollmodel', login_url='login')
def add_payroll(request):
    if request.method == "GET":
        form = PayrollForm()
        return render(request,'payroll_create.html',{'form':form})
    if request.method == "POST":
        form = PayrollForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            employee = form.cleaned_data.get('employee')
            job = form.cleaned_data.get('job')
            department = form.cleaned_data.get('department')
            salary = form.cleaned_data.get('salary')
            pay_date = form.cleaned_data.get('pay_date')
            tags = form.cleaned_data.get('tags')
            payroll = PayrollModel.objects.create(
                name=name,
                employee=employee,
                job=job,
                department=department,
                salary=salary,
                pay_date=pay_date
            )
            payroll.tags.set(tags)
            payroll.save()
            messages.success(request, 'Form saved successfully.')
            return redirect('/hr_payroll/show_payroll/')

@permission_required('hr_payroll.change_payrollmodel', login_url='login')
def update_payroll(request, payroll_id):
    payroll = PayrollModel.objects.get(id=payroll_id)
    if request.method == "GET":
        values = {
            'name': payroll.name,
            'employee': payroll.employee,
            'job': payroll.job,
            'department': payroll.department,
            'salary': payroll.salary,
            'pay_date': payroll.pay_date,
            'tags': payroll.tags.all()
        }
        form = PayrollForm(initial=values)
        context = {'form': form, 'payroll': payroll}
        return render(request, 'payroll_update.html', context)
    elif request.method == "POST":
        form = PayrollForm(request.POST)
        if form.is_valid():
            payroll.name = form.cleaned_data.get('name')
            payroll.employee = form.cleaned_data.get('employee')
            payroll.job = form.cleaned_data.get('job')
            payroll.department = form.cleaned_data.get('department')
            payroll.salary = form.cleaned_data.get('salary')
            payroll.pay_date = form.cleaned_data.get('pay_date')
            payroll.tags.set(form.cleaned_data.get('tags'))
            payroll.save()
            messages.success(request, 'Form updated successfully.')
            return redirect('/hr_payroll/detail/' + str(payroll_id) + '/')

@permission_required('hr_payroll.delete_payrollmodel', login_url='login')
def delete_payroll(request, payroll_id):
    if request.method == "GET":
        payroll = PayrollModel.objects.get(id=payroll_id)
        payroll = PayrollModel.objects.filter(id=payroll_id)
        payroll.delete()
        messages.success(request, 'Form deleted successfully.')
        return redirect('/hr_payroll/show_payroll/')