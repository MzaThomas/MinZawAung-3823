from django.db import models

# Create your models here.
from django.utils import timezone
from hr_employees.models import EmployeeModel
from hr_jobs.models import JobModel
from hr_departments.models import DepartmentModel
from hr_tags.models import AttendanceTagModel

class AttendanceModel(models.Model):
	class Meta:
		permissions = (
			("view_attendancemodel", "Can view attendance model"),
			)
	name = models.CharField(max_length=20, verbose_name='Name')
	employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE, default=None)
	job = models.ForeignKey(JobModel, on_delete=models.CASCADE, default=None)
	department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE, default=None)
	date = models.DateField(verbose_name='Date', default=timezone.now)
	tags = models.ManyToManyField(AttendanceTagModel)

	def __str__(self):
		return self.name
