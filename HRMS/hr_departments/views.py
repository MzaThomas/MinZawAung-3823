from django.shortcuts import render, redirect
from .models import DepartmentModel
from .forms import DepartmentForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator
# Create your views here.

class SearchBy(View):

    def get(self, request):
        search = request.GET.get('search')
        if search:    
            departments = DepartmentModel.objects.filter(
                Q(name__icontains=search) | 
                Q(sequence__icontains=search) |
                Q(meeting_date__icontains=search) |
                Q(total_employees__icontains=search) |
                Q(note__icontains=search) |
                Q(status__icontains=search) |
                Q(create_date__icontains=search)
            )
        else:      
            departments = DepartmentModel.objects.all()
        return render(request, 'department_list.html', {'page_obj': departments})

class OrderBy(View):

    def get(self, request):
        order = request.GET.get('order')
        departments = DepartmentModel.objects.all().order_by("-"+ order)
        order_selected = {str(order): 'btn-primary text-white'}

        paginator = Paginator(departments, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'department_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

class Department(PermissionRequiredMixin, View):
	permission_required = 'hr_departments.view_departmentmodel'
	login_url = 'login'
	def get(self, request, department_id):
		department = DepartmentModel.objects.get(id=department_id)
		return render(request,'department_detail.html', {'department': department})

class AllDepartments(LoginRequiredMixin, View):
	login_url = 'login'
	def get(self, request):
		all_departments = DepartmentModel.objects.all()
		paginator = Paginator(all_departments, 3)
		page_number = request.GET.get('page')
		page_obj = paginator.get_page(page_number)
		return render(request,'department_list.html', {'page_obj': page_obj})

class AddDepartment(PermissionRequiredMixin, View):
	permission_required = 'hr_departments.add_departmentmodel'
	login_url = 'login'
	def get(self, request):
		form = DepartmentForm()
		return render(request,'department_create.html',{'form':form})
	def post(self, request):
		form = DepartmentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Form saved successfully.')
			return redirect('/hr_departments/show_department/')

class UpdateDepartment(PermissionRequiredMixin, View):
	permission_required = 'hr_departments.change_departmentmodel'
	login_url = 'login'
	def get(self, request, department_id):
		department = DepartmentModel.objects.get(id=department_id)
		form = DepartmentForm(instance=department)
		return render(request, 'department_update.html', {'form': form, 'uploaded_image':
		department.attachment})
	def post(self, request, department_id):
		department = DepartmentModel.objects.get(id=department_id)
		form = DepartmentForm(request.POST, request.FILES, instance=department)
		if form.is_valid():
			form.save()
			messages.success(request, 'Form updated successfully.')
			return redirect('/hr_departments/detail/' + str(department_id) + '/')

class DeleteDepartment(PermissionRequiredMixin, View):
	permission_required = 'hr_departments.delete_departmentmodel'
	login_url = 'login'
	def get(self, request, department_id):
		department = DepartmentModel.objects.filter(id=department_id)
		department.delete()
		messages.success(request, 'Form deleted successfully.')
		return redirect('/hr_departments/show_department/')