total_cost = float(input('Enter the cost of your dream home (in $): '))
portion_down_payment = 0.25
annual_salary = float(input('Enter your annual salary (in $): ')) # getting directly the monthly_salary is more easy to understand
monthly_salary = annual_salary / 12
portion_saved = float(input('Enter the percent of your salary to save each month (in %): ')) / 100
r = 0.04    # annual return rate

current_saving = 0
month = 0
while current_saving < portion_down_payment * total_cost:   # portion_down_payment = 0 will cause an infinite loop
    # First the return of investment would be calculated, consider first month for instance to why
    # then salary would be added to the investment
    current_saving += current_saving * r / 12
    current_saving += monthly_salary * portion_saved
    # if this process is done, one month is passed
    month += 1
print(f'{month} months it will take you to save up enough money for down payment of your dream house.')