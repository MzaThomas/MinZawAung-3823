from django import forms
from django.forms import widgets
from hr_employees.models import EmployeeModel
from hr_jobs.models import JobModel
from hr_departments.models import DepartmentModel
from hr_tags.models import PayrollTagModel

class PayrollForm(forms.Form):
	name = forms.CharField(max_length=20, label='Enter Name', widget=widgets.TextInput(attrs={'placeholder':'Your Name', 'class': 'form-control'}))
	employee = forms.ModelChoiceField(queryset=EmployeeModel.objects.all(), widget=widgets.Select(attrs={'class': 'form-control'}))
	job = forms.ModelChoiceField(queryset=JobModel.objects.all(), widget=widgets.Select(attrs={'class': 'form-control'}))
	department = forms.ModelChoiceField(queryset=DepartmentModel.objects.all(), widget=widgets.Select(attrs={'class': 'form-control'}))
	salary = forms.CharField(label='Enter Salary', widget=widgets.TextInput(attrs={'placeholder':'Your Salary', 'class': 'form-control'}))
	pay_date = forms.DateField(label='Enter Pay Date', widget=widgets.DateInput(attrs={'type':'date', 'class': 'form-control'}))
	tags = forms.ModelMultipleChoiceField(queryset=PayrollTagModel.objects.all(), widget=widgets.CheckboxSelectMultiple())