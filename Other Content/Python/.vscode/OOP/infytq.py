class Employee:
    def __init__(self):
        self.employee_id = None
    def check_eligibility(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("The employee is eligible for special benefits")
        else:
            print("The employee is not eligible for special benefits")
emp1=Employee()
emp1.employee_id=10000
emp1.check_eligibility()
emp2=Employee()
emp2.employee_id=4500
emp2.check_eligibility()