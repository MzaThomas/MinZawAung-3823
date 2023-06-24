from django.urls import path
from hr_payroll import views
# from app_name import file_name

urlpatterns = [
    path('show_payroll/', views.all_payrolls),
    path('new_payroll/', views.add_payroll),
    path('update/<int:payroll_id>/', views.update_payroll),
    path('detail/<int:payroll_id>/', views.payroll),
    path('delete/<int:payroll_id>/', views.delete_payroll),
    path('search_by/', views.search_by),
    path('order_by/', views.order_by)
    # path('domain_name/', file_name.function_name)
]