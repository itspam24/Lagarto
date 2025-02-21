class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount 

    def display_employee(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₱{self.salary:.2f}")
        print("-" * 20)

employee = Employee(name="Hera Ai", position="Baker", salary=16959)

print("Initial Employee Details:")
employee.display_employee()

employee.give_raise(5000)

print("Employee Details After Raise:")
employee.display_employee()