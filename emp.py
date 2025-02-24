print("Welcome to Employee Wage Computation")

import random

def check_attendance():
    """
     Descripition : this function will check attendance for the employee
    Parameter: none
    Return : attendance
    """
    print("Welcome to Employee Wages Computation program on master branch")
    attendance = random.choice([0, 1, 2])
    
    if attendance == 1:
        print("The Employee is present for full time")
    elif attendance == 2:
        print("The Employee is present for half time")
    else:
        print("The Employee is absent")

    return attendance

def cal_daily_wage(wage_per_hour = 20):
    
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

def wage_till_condition(max_hours = 100 ,max_days = 20,wage_per_hour =20):
    """
    Descripition : this function will calculate wages unit max_hour and max_days are reached
    Parameter: max_hours, max_days,wage_per_ hour.
    Return : toalt wage after max_hous and max_day
    """

    total_wage = 0
    total_hour = 0
    total_days = 0

    while total_hour < max_hours and total_days < max_days:
        daily_wage = cal_daily_wage(wage_per_hour)
        total_wage += daily_wage

        attendance  =  check_attendance()

        if attendance == 1:
            total_hour +=8
        elif attendance == 2:

            total_hour +=4
        total_days +=1
        print(f"day {total_days}: Daily wage ={daily_wage}, total hour ={total_hour}, total_wage = {total_wage}")

    print("calculation finished.")
    print(f"Total days worked: {total_days}")
    print(f"Total hours worked: {total_hour}")
    print(f"Total wage: {total_wage}")
    return total_wage

if __name__ =="__main__":
    wage_till_condition()

    
    



