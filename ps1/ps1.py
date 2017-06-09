"""
This program finds out the amount of time to save
for house down payment.
"""




annual_salary = input('Enter your annual salary: ')
portion_saved = input('Enter the percent of your salary to save, as a decimal: ')
total_cost = input('Enter cost of your dream home: ')
current_savings = 0
portion_down_payment = int(total_cost)*.25
monthly_salary = int(annual_salary)/12
months = 0
r = .04
print(portion_down_payment)

while current_savings <= portion_down_payment:
    current_savings += float(portion_saved) * monthly_salary
    current_savings += (current_savings*r)/12
    months += 1

print(months)
