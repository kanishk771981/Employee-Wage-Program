import random

class EmployeeWage:
    def __init__(self, name, wage_per_hour, max_hours, max_days):
        self.name = name
        self.wage_per_hour = wage_per_hour  # Wage per hour specific to company
        self.max_hours = max_hours  # Max hours per month specific to company
        self.max_days = max_days  # Max days per month specific to company
        self.total_wage = 0
        self.total_hours = 0
        self.total_days = 0

    def check_attendance(self):
        """Checks employee attendance and returns 0 for absent, 1 for full-time, 2 for half-time"""
        attendance = random.choice([0, 1, 2])
        return attendance

    def calculate_daily_wage(self, attendance):
        """Calculates daily wage based on attendance"""
        if attendance == 1:
            return self.wage_per_hour * 8  # Full-time
        elif attendance == 2:
            return self.wage_per_hour * 4  # Half-time
        return 0  # Absent

    def calculate_wages_till_condition(self):
        """Calculates wages until max_hours or max_days are reached."""
        while self.total_hours < self.max_hours and self.total_days < self.max_days:
            attendance = self.check_attendance()
            daily_wage = self.calculate_daily_wage(attendance)
            
            self.total_wage += daily_wage
            if attendance == 1:
                self.total_hours += 8
            elif attendance == 2:
                self.total_hours += 4

            self.total_days += 1

        return self.total_wage

    @classmethod
    def compute_employee_wage(cls, name, wage_per_hour, max_hours, max_days):
        """Computes employee wage for a given company using parameters instead of class variables"""
        employee = cls(name, wage_per_hour, max_hours, max_days)
        return employee.calculate_wages_till_condition()


# Example Usage: Different companies with different wages and working conditions
if __name__ == "__main__":
    print("Welcome to Employee Wage Computation")

    # Company 1
    total_wage_mindsprit = EmployeeWage.compute_employee_wage("Alice", wage_per_hour=25, max_hours=90, max_days=18)
    print(f"Total wage for Alice (mindsprit): {total_wage_mindsprit}")

    print("-" * 20)

    # Company 2
    bob = EmployeeWage("Bob", wage_per_hour=30, max_hours=100, max_days=20)
    bob_wage = bob.calculate_wages_till_condition()
    print(f"Total wage for Bob (TCS): {bob_wage}")

    
    



