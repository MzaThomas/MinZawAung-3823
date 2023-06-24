from django.shortcuts import render, redirect
from .models import ExpenseModel
from .forms import ExpenseForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.

class SearchBy(View):

    def get(self, request):
        search = request.GET.get('search')
        if search:    
            expenses = ExpenseModel.objects.filter(
                Q(name__icontains=search) | 
                Q(description__icontains=search) |
                Q(paid_by__icontains=search) |
                Q(total_expense__icontains=search) |
                Q(expense_date__icontains=search)
            )
        else:      
            expenses = ExpenseModel.objects.all()
        return render(request, 'expense_list.html', {'page_obj': expenses})

class OrderBy(View):

    def get(self, request):
        order = request.GET.get('order')
        expenses = ExpenseModel.objects.all().order_by("-"+ order)
        order_selected = {str(order): 'btn-primary text-white'}

        paginator = Paginator(expenses, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'expense_list.html', {'page_obj': page_obj, 'order_selected': order_selected})

class AllExpenses(LoginRequiredMixin, View):
    login_url = 'login'

    def get(self, request):
        all_expenses = ExpenseModel.objects.all()

        paginator = Paginator(all_expenses, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'expense_list.html', {'page_obj': page_obj})
        # return render(request,'expense_list.html', {'all_expenses': all_expenses})

class Expense(PermissionRequiredMixin, View):
    permission_required = 'hr_expenses.view_expensemodel'
    login_url = 'login'

    def get(self, request, expense_id):
        expense = ExpenseModel.objects.get(id=expense_id)  
        return render(request,'expense_detail.html', {'expense': expense})

class AddExpense(PermissionRequiredMixin, View):
    permission_required = 'hr_expenses.add_expensemodel'
    login_url = 'login'

    def get(self, request):
        form = ExpenseForm()
        return render(request,'Expense_create.html',{'form':form}) 
    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():  
            form.save()
            messages.success(request, 'Form saved successfully.')
            return redirect('/hr_expenses/show_expense/')

class UpdateExpense(PermissionRequiredMixin, View):
    permission_required = 'hr_expenses.change_expensemodel'
    login_url = 'login'

    def get(self, request, expense_id):
        expense = ExpenseModel.objects.get(id=expense_id)  
        form = ExpenseForm(instance=expense)
        return render(request, 'expense_update.html', {'form': form})
    def post(self, request, expense_id):
        expense = ExpenseModel.objects.get(id=expense_id)  
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form updated successfully.')
            return redirect('/hr_expenses/detail/' + str(expense_id) + '/')

class DeleteExpense(PermissionRequiredMixin, View):
    permission_required = 'hr_expenses.delete_expensemodel'
    login_url = 'login'

    def get(self, request, expense_id):
        expense = ExpenseModel.objects.filter(id=expense_id)
        expense.delete()
        messages.success(request, 'Form deleted successfully.')
        return redirect('/hr_expenses/show_expense/')