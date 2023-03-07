total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
starting_annual_salary = float(input('Enter the starting annual salary (in $): '))
starting_monthly_salary = starting_annual_salary / 12
semi_annual_raise = 0.07
r = 0.04    # annual return rate

low = 0
high = 10000
# the precision of portion_saved is 0.0001
# we work with int_portion_saved which is portion_saved * 10000, instead of real number of portion_saved
# first guess for int_portion_saved
int_portion_saved = int((low + high) / 2)

current_saving = 0
for month in range(36):
    current_saving += current_saving * r / 12
    monthly_salary = starting_monthly_salary * (1 + semi_annual_raise)**(int(month / 6))
    current_saving += monthly_salary * (int_portion_saved / 10000)  # portion_saved = int_portion_saved / 10000
# saved money after 36 month
final_saving = current_saving

bisection_epoch = 1
while abs(final_saving - down_payment) > 100 and high - low != 1:
    # determine whether int_portion_saved is high or low, then choose the bisection
    if final_saving < down_payment:
        low = int_portion_saved
    else:
        high = int_portion_saved
    # new guess in the choosen bisection
    int_portion_saved = int((low + high) / 2)
    # calculate how much money will be saved for a specific int_portion_saved
    # assume we are not allowed to define and use functions here
    current_saving = 0
    for month in range(36):
        current_saving += current_saving * r / 12
        monthly_salary = starting_monthly_salary * (1 + semi_annual_raise)**(int(month / 6))
        current_saving += monthly_salary * (int_portion_saved / 10000)
    final_saving = current_saving

    bisection_epoch += 1
# if bisection_epoch is smaller than 15, then we've got to the answer
if bisection_epoch < 15:
    print('Best saving rate', int_portion_saved / 10000)
    print('Steps in bisection search', bisection_epoch)
else:   # answer is not in the portion_saved interval [0.0000, 1.0000), which means the salary is not enough
    print('With your salary, it is not possible to pay the down payment in three years, sorry!')
    print('epochs', bisection_epoch)
# you can try out 66100, 66140, 66150, 66200, 66300, 66400, 66500 for starting_annual_salary 's
# If you want to be more precise, you can set
# low = 1
# high = 10001
# at the beginning of the program
# because answer 0.0000 is impossible to obtain, and 1.0000 should be possible
# which means: portion_saved interval should be (0.0000, 1.0000]