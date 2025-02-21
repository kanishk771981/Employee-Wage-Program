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

if __name__ == "__main__":  # Fixed syntax error
    check_attendance()

