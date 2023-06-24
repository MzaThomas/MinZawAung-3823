from django import forms
from django.forms import widgets
from .models import ExpenseModel
from hr_tags.models import ExpenseTagModel
from hr_employees.models import EmployeeModel
from hr_departments.models import DepartmentModel

PAIDBY_CHOICES =(
    ('Company', 'Company'),
    ('Employee', 'Employee')
    )


class ExpenseForm(forms.ModelForm):
    
    class Meta:
        model = ExpenseModel
        fields = "__all__"
        labels  = {
            'name':'Enter Name',
            'employee':'Enter Employee', 
            'department':'Enter Department',  
            'description':'Enter Description',
            'total_expense':'Enter Total Expense', 
            'paid_by':'Paid By', 
            'expense_date':'Enter Expense Date'
        }

        widgets = {
            'name': widgets.TextInput(attrs={'placeholder':'Name','class': 'form-control'}),
            'employee': widgets.Select(attrs={'class': 'form-control'}),
            'department': widgets.Select(attrs={'class': 'form-control'}),
            'description': widgets.TextInput(attrs={'placeholder':'Description','class': 'form-control'}),
            'total_expense': widgets.TextInput(attrs={'placeholder':'Total Expense','class': 'form-control'}),
            'paid_by': widgets.Select(choices=PAIDBY_CHOICES, attrs={'class' : 'form-control'}),
            'expense_date': widgets.DateInput(attrs={'placeholder':'Submit Date', 'type': 'date','class': 'form-control'}),
            'tags': widgets.CheckboxSelectMultiple()
        }