"""
This program finds out the amount of time to save
for house down payment.
"""




annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
current_savings = 0
portion_down_payment = total_cost*.25
monthly_salary = annual_salary/12
months = 0
r = .04
num_months = int(input('Enter number of months to save down payments: '))
print(portion_down_payment)

while current_savings <= portion_down_payment:
    current_savings += round((portion_saved * monthly_salary), 2)
    current_savings += round(((current_savings*r)/12), 2)
    months += 1
    if months % 6 == 0:
        annual_salary += round((annual_salary * semi_annual_raise),2)
        monthly_salary = round((annual_salary/12), 2)

print(months)
