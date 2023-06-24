from django import forms
from hr_departments import models
from django.forms import widgets

RESOURCES_CHOICES =(
	('normal', 'Normal'),
	('excess', 'Excess'),
	('not enough', 'Not enough')
	)
STATUS_CHOICES =(
	('draft', 'Draft'),
	('open', 'Open'),
	('confirm', 'Confirm')
)

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = models.DepartmentModel
		fields = "__all__"
		
		labels = {
			'name':'Enter Name',
			'sequence':'Enter Sequencce',
			'meeting_date':'Enter Meeting Date',
			'total_employees':'Enter Total Employees',
			'monthly_expenses':'Enter Monthly Expenses',
			'note':'Enter Note',
			'resources':'Enter Resources',
			'status':'Enter Status',
			'is_active':'Is Active',
			'create_date':'Enter Crate Date',
			'attachment':'Upload Attachment'
		}

		widgets = {
			'name': widgets.TextInput(attrs={'placeholder':'Name', 'class': 'form-control'}),
			'sequence': widgets.NumberInput(attrs={'placeholder':'Sequence', 'class': 'form-control'}),
			'total_employees': widgets.TextInput(attrs={'placeholder':'Total Employees', 'class': 'form-control'}),
			'monthly_expenses': widgets.TextInput(attrs={'placeholder':'Monthly Expenses', 'class': 'form-control'}),
			'meeting_date': widgets.DateInput(attrs={'placeholder':'Meeting Date', 'type':
			'date', 'class': 'form-control'}),
			'note': widgets.TextInput(attrs={'placeholder':'Note', 'class': 'form-control'}),
			'resources': widgets.Select(choices=RESOURCES_CHOICES, attrs={'class' : 'form-control'}),
			'status': widgets.Select(choices=STATUS_CHOICES, attrs={'class' : 'form-control'}),
			'is_active': widgets.CheckboxInput(),
			'create_date': widgets.DateTimeInput(attrs={'type':'datetime-local', 'class': 'form-control'}),
			'attachment': widgets.ClearableFileInput()
		}