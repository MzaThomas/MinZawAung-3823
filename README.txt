Welcome to Human Resource Management System!

In this project, I added new column to former tables(hr_employees, hr_contracts, hr_jobs, hr_departments, hr_recruitments, hr_tags) 
and new apps or tables(hr_attendance, hr_payroll, hr_expenses).
So, you have to do "makemigrations" and "migrate" all of them.

Hr_employees - I added 3 new columns. Email, Phone Number and Tenure. 
		Email is to fill email address.
		Phone Number is to fill phone number.
		Tenure is to fill your duration of month working in this company.

Hr_contracts - I added 2 new columns. Email and Duration.
		Email is to fill email address.
		Duration is to fill the duration of month between Start Date and End Date.

Hr_jobs      - I added 1 new column. Total.
		Total means Total Employee.
		It is to show total employee with the job(Senior, Junior, Frontend, etc.) in the company.

Hr_departments - I added 2 new columns. Monthly Expenses and Resources.
		Monthly is to show the monthly expenses of each department.
		Resources is to show whether the resources of each department are excess, not enough or normal.
		So that the company can see the finanicial condition of each department.

Hr_recruitments - I added 2 new columns. Experience and Expected Salary.
		Experience is to show the duration of months experience in this job.
		Expected Salary is to show the expected salary of interviewry.

Hr_attendance - I created new table.
		The table has 5 columns. Name, Empolyee, Department, Job and Date.
		Name is the name of the employee.
		Employee is the name of the employee to choose. I connected this with hr_employees model(ManyToOne).
		Job is the name of the job to choose. I connected this with hr_jobs model(ManyToOne).
		Department is the name of the department to choose. I connected this with hr_departments model(ManyToOne).
		Date is to show the attendance date.

Hr_payroll - I created new table.
		The table has 6 columns. Name, Employee, Job, Department, Salary and Pay Date.
		Name is the name of the employee.
		Employee is the name of the employee to choose. I connected this with hr_employees model(ManyToOne).
		Job is the name of the job to choose. I connected this with hr_jobs model(ManyToOne).
		Department is the name of the department to choose. I connected this with hr_departments model(ManyToOne).
		Salary is the monthly salary of the chosen employee.
		Pay Date is the date that the salary is monthly paid.

Hr_expenses - I created new table.
		The table has 7 columns. Name, Employee, Department, Description, Total Expense, Paid By and Expense Date.
		Name is the name of the employee who paid for expenses.
		Employee is the name of the employee to choose. I connected this with hr_employees model(ManyToOne).
		Department is the name of the department to choose. I connected this with hr_departments model(ManyToOne).
		Description is the reason of expense(Customer catering, etc..)
		Total Expense is the total cost of above description.
		Paid By is to choose whether the expense is already paid by company or paid by employee.
		Expense Date is the date of the expense.

Hr_tags - I added 3 new tables to create ManyToMany fields in hr_attendance, hr_payroll and hr_expenses.
	In AttendanceTagModel, you can add "Present", "Absent", "Present but late", "Absent with Permit", etc.. to show the employees' presence and absence.
	In PayrollTagModel, you can add "Paid", "Pre-Paid", "Half-Paid", "Unpaid", etc.. to show whether the employees' salary is paid or unpaid.
	In ExpenseTagModel, you can add "To Submit", "Submitted", etc.. to show expense status.

And also, I change the design of login and some other minor design.

I add some new features. When you create, update or delete a form, there will be a line saying like "Form Created or Updated or Deleted Successfully" like success message.

When you update or delete the form, there will be a pop up for confirmation that says "Are you sure you want to update or delete this form?".

That's all about my project. Thank You!