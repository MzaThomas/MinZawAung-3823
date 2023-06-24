from django.db import models

# Create your models here.
from django.utils import timezone
from hr_employees.models import EmployeeModel
from hr_jobs.models import JobModel
from hr_departments.models import DepartmentModel
from hr_tags.models import PayrollTagModel

class PayrollModel(models.Model):
	class Meta:
		permissions = (
			("view_payrollmodel", "Can view payroll model"),
			)

	name = models.CharField(max_length=20, verbose_name='Name')
	employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
	job = models.ForeignKey(JobModel, on_delete=models.CASCADE, default=None)
	department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=None)
	salary = models.CharField(max_length=50, verbose_name='Salary', default=None)
	pay_date = models.DateField(verbose_name='Pay Date', default=timezone.now)
	tags = models.ManyToManyField(PayrollTagModel)

	def __str__(self):
		return self.name