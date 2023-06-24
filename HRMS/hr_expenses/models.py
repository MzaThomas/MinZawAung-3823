from django.db import models

# Create your models here.
from django.utils import timezone
from hr_tags.models import ExpenseTagModel
from hr_employees.models import EmployeeModel
from hr_departments.models import DepartmentModel

class ExpenseModel(models.Model):
	class Meta:
		permissions = (
			("view_expensemodel", "Can view expense model"),
			)

	name = models.CharField(max_length=50, verbose_name='Name', default=None)
	employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
	department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=None)
	description = models.CharField(max_length=50, verbose_name='Description')
	total_expense = models.CharField(max_length=50, verbose_name='Total Expense', default=None)
	paid_by = models.CharField(max_length=50, verbose_name='Paid By', default='Company')
	expense_date = models.DateField(verbose_name='Expense Date', default=timezone.now)
	tags = models.ManyToManyField(ExpenseTagModel)

	def __str__(self):
		return self.name