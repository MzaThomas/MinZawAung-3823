from django.urls import path
from hr_expenses import views

urlpatterns = [
	path('show_expense/', views.AllExpenses.as_view()),
    path('new_expense/', views.AddExpense.as_view()),
    path('update/<int:expense_id>/', views.UpdateExpense.as_view()),
    path('delete/<int:expense_id>/', views.DeleteExpense.as_view()),
    path('detail/<int:expense_id>/', views.Expense.as_view()),
    path('search_by/', views.SearchBy.as_view()),
    path('order_by/', views.OrderBy.as_view())
    #path('domin_name/', file_name.class_name.as_view())
]