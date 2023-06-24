"""hrms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from hr_employees import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),

    path('hr_employees/', include('hr_employees.urls')),
    path('hr_contracts/', include('hr_contracts.urls')),
    path('hr_jobs/', include('hr_jobs.urls')),
    path('hr_departments/', include('hr_departments.urls')),
    path('hr_recruitments/', include('hr_recruitments.urls')),
    path('hr_attendance/', include('hr_attendance.urls')),
    path('hr_payroll/', include('hr_payroll.urls')),
    path('hr_expenses/', include('hr_expenses.urls'))
    # path('app_name/', include('app_name.file_name'))
]
