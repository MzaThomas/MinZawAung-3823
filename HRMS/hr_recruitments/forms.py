from django import forms
from django.forms import widgets
from .models import ResumeModel
from hr_employees.models import EmployeeModel
from hr_tags.models import ResumeTagModel

STATUS_CHOICES =(
	('draft', 'draft'),
	('Confirm', 'confirm'),
	('Cancel', 'cancel')
)
class ResumeForm(forms.ModelForm):
	class Meta:
		model = ResumeModel
		fields = "__all__"
		labels = {
			'name':'Enter Name',
			'sequence':'Enter Sequence',
			'experience':'Enter Experience(Month)',
			'expected_salary':'Enter Expected Salary',
			'appointment_date':'Enter Appointment Date',
			'note':'Internal Note',
			'status':'Status',
			'is_active':'Is Active',
			'create_date':'Enter Create Date',
			'attachment':'Upload Attachment'
		}
		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Resume Name', 'class': 'form-control'}),
			'sequence': widgets.NumberInput(attrs={'placeholder':'0', 'class': 'form-control'}),
			'experience': widgets.NumberInput(attrs={'placeholder':'0', 'class': 'form-control'}),
			'expected_salary': widgets.TextInput(attrs={'placeholder':'Expected Salary', 'class': 'form-control'}),
			'appointment_date': widgets.DateInput(attrs={'placeholder':'Enter Appointment Date', 'type': 'date', 'class': 'form-control'}),
			'note': widgets.TextInput(attrs={'placeholder':'Internal Note', 'class': 'form-control'}),
			'status': widgets.Select(choices=STATUS_CHOICES),
			'is_active': widgets.CheckboxInput(),'create_date': widgets.DateTimeInput(attrs={'type':'datetime-local', 'class': 'form-control'}),
			'attachment': widgets.ClearableFileInput(),
			'employee': widgets.Select(attrs={'class': 'form-control'}),
			'tags': widgets.CheckboxSelectMultiple()
		}