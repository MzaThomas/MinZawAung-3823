from django.db import models

# Create your models here.
from django.utils import timezone
from hr_jobs.models import JobModel
from hr_tags.models import EmployeeTagModel

class EmployeeModel(models.Model):
	class Meta:
		permissions = (
		("view_employeemodel", "Can view employee model"),
		)

	name = models.CharField(max_length=20, verbose_name='Name')
	age = models.IntegerField(verbose_name='Age')
	birthday = models.DateField(verbose_name='Birthday', default=timezone.now)
	address = models.TextField(max_length=100, verbose_name='Address')
	email = models.EmailField(max_length=50, default='test@gmail.com')
	phone_number = models.CharField(max_length=20, verbose_name='Phone Number', default=None)
	gender = models.CharField(max_length=10, verbose_name='Gender', default='other')
	is_married = models.BooleanField(verbose_name='Is Married', default=False)
	joining_date = models.DateTimeField(verbose_name='Joining Date', default=timezone.now)
	tenure = models.IntegerField(verbose_name="Tenure(Month)", default=0)
	image = models.ImageField(verbose_name='Image', default=None)
	job = models.ForeignKey(JobModel, on_delete=models.CASCADE, default=None)
	tags = models.ManyToManyField(EmployeeTagModel)

	def __str__(self):
		return self.name