from django import forms
from django.forms import widgets
from hr_employees.models import EmployeeModel
from hr_jobs.models import JobModel
from hr_departments.models import DepartmentModel
from hr_tags.models import AttendanceTagModel

class AttendanceForm(forms.Form):
	name = forms.CharField(max_length=20, label='Enter Name', widget=widgets.TextInput(attrs={'placeholder':'Your Name', 'class': 'form-control'}))
	employee = forms.ModelChoiceField(queryset=EmployeeModel.objects.all(), widget=widgets.Select(attrs={'class': 'form-control'}))
	job = forms.ModelChoiceField(queryset=JobModel.objects.all(), widget=widgets.Select(attrs={'class': 'form-control'}))
	department = forms.ModelChoiceField(queryset=DepartmentModel.objects.all(), widget=widgets.Select(attrs={'class': 'form-control'}))
	date = forms.DateField(label='Enter Date', widget=widgets.DateInput(attrs={'type':'date', 'class': 'form-control'}))
	tags = forms.ModelMultipleChoiceField(queryset=AttendanceTagModel.objects.all(), widget=widgets.CheckboxSelectMultiple())