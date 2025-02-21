print("Welcome to Employee Wage Computation")

import random

def check_attendance():
    print("Welcome to Employee Wages Computation program on master branch")
    attendance = random.choice([0, 1, 2])
    
    if attendance == 1:
        print("The Employee is present for full time")
    elif attendance == 2:
        print("The Employee is present for half time")
    else:
        print("The Employee is absent")

    return attendance

def cal_daily_wage():
    wage_per_hour = 20
    emp_check = check_attendance()

    match emp_check:
        case 0:
         daily_wage = 0
         print(f"Employee is absent  for full day so daily wage is : {daily_wage}")

        case 1:
            daily_wage = wage_per_hour * 8
            print(f"Employee is present for full day so daily wage is : {daily_wage}")

        case 2:
            daily_wage = wage_per_hour*4
            print(f"Employee is present for half-day so daily wage is : {daily_wage}")


    return daily_wage

def monthly_wage():
    total_wage = 0
    for i in range (20):
        total_wage = total_wage + cal_daily_wage()

    return total_wage


if __name__ =="__main__":
    monthly_wage()
    




