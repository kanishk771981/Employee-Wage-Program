print("Welcome to Employee Wage Computation")

import random

class EmployeeWage:
    # Represents an employee and calculates their wages.

    WAGE_PER_HOUR = 20  # Class variable for wage per hour
    MAX_HOURS = 100     # Class variable for maximum hours
    MAX_DAYS = 20      # Class variable for maximum days

    def __init__(self, name):
        self.name = name
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0

    def check_attendance(self):
        #Checks employee attendance and returns 0 for absent, 1 for full-time, 2 for half-time
        print("Welcome to Employee Wages Computation program on master branch")  
        attendance = random.choice([0, 1, 2])
        if attendance == 1:
            print("The Employee is present for full time")
        elif attendance == 2:
            print("The Employee is present for half time")
        else:
            print("The Employee is absent")
        return attendance

    def calculate_daily_wage(self):
        #Calculates daily wage based on attendance.
        emp_check = self.check_attendance()
        daily_wage = 0

        match emp_check:
            case 0:
                print(f"{self.name} is absent for full day so daily wage is : 0")
            case 1:
                daily_wage = EmployeeWage.WAGE_PER_HOUR * 8
                print(f"{self.name} is present for full day so daily wage is : {daily_wage}")
            case 2:
                daily_wage = EmployeeWage.WAGE_PER_HOUR * 4
                print(f"{self.name} is present for half-day so daily wage is : {daily_wage}")

        return daily_wage

    def calculate_wages_till_condition(self):
        #Calculates wages until max_hours or max_days are reached.

        while self.total_hours < EmployeeWage.MAX_HOURS and self.total_days < EmployeeWage.MAX_DAYS:
            daily_wage = self.calculate_daily_wage()
            self.total_wage += daily_wage

            attendance = self.check_attendance()

            if attendance == 1:
                self.total_hours += 8
            elif attendance == 2:
                self.total_hours += 4
            self.total_days += 1
            print(f"Day {self.total_days}: Daily wage = {daily_wage}, Total hours = {self.total_hours}, Total wage = {self.total_wage}")

        print("Calculation finished.")
        print(f"Total days worked: {self.total_days}")
        print(f"Total hours worked: {self.total_hours}")
        print(f"Total wage: {self.total_wage}")
        return self.total_wage

    @classmethod
    def compute_employee_wage(cls, name):
        #Computes employee wage using the class variables.
        
        employee = EmployeeWage(name)
        return employee.calculate_wages_till_condition()


if __name__ == "__main__":
    print("Welcome to Employee Wage Computation")

    total_wage_alice = EmployeeWage.compute_employee_wage("Alice")
    print(f"Total wage for Alice (using class method): {total_wage_alice}")

    print("-" * 20)

    bob = EmployeeWage("Bob")
    bob_wage = bob.calculate_wages_till_condition()  # Capture the return value
    print(f"Total wage for Bob (using instance methods): {bob_wage}") # Print the captured value.

    
    



