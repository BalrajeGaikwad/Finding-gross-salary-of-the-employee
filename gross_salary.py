"""

In a company an employee is paid as under:   If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary. 
If his salary is either equal to or above Rs. 1500, then HRA Rs. 500 and DA = 98% of basic salary. 
If the employee's salary is input through the keyboard write a program to find his gross salary.

"""

# 1) HRA: House Rent Allowance
# 2) DA: Dearness Allowance

# 3) gross salary= Basic salary + HRA + DA

basic_salary=int(input("Enter the basic salary of employee :- "))

if(basic_salary<1500):
    HRA=basic_salary*10/100
    DA=basic_salary*90/100
else:
    HRA=500
    DA=basic_salary*90/100

gross_salary=basic_salary+HRA+DA
print("gross_salary of the employee is :--", gross_salary)
