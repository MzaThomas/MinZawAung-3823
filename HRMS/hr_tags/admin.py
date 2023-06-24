from django.contrib import admin
from .models import JobTagModel
from .models import EmployeeTagModel
from .models import ContractTagModel
from .models import ResumeTagModel
from .models import AttendanceTagModel
from .models import PayrollTagModel
from .models import ExpenseTagModel

# Register your models here.
admin.site.register(JobTagModel)
admin.site.register(EmployeeTagModel)
admin.site.register(ContractTagModel)
admin.site.register(ResumeTagModel)
admin.site.register(AttendanceTagModel)
admin.site.register(PayrollTagModel)
admin.site.register(ExpenseTagModel)