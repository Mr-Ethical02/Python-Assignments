'''
To calculate salary of an employee given his basic pay (take as input from user). Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary payable after deductions. 
'''

basic_salary = int(input("Enter Basic Salary: "))
HRA = round((basic_salary)/10)
TA = round((basic_salary)/20)
gross_sal = basic_salary + HRA + TA
tax = round((basic_salary)/50)
net_sal = basic_salary - tax - TA - HRA

print("Gross Salary is:",gross_sal,"\nHRA is:",HRA,"\nTA is:",TA,"\nTax Payable is:",tax,"\nNet Salary is:",net_sal)