import csv
import sys

class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: ₹{self.salary}"

class EmployeeSystem:
    def __init__(self, filename):
        self.filename = filename
        self.employees = []
        self.load_employees()

    def load_employees(self):
        """Read employee records from CSV file"""
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    emp_id = row['EmployeeID']
                    name = row['Name']
                    department = row['Department']
                    salary = row['Salary']
                    self.employees.append(Employee(emp_id, name, department, salary))
        except FileNotFoundError:
            print(f"Error: {self.filename} file not found!")

    def display_all(self):
        """Display all employee records"""
        if not self.employees:
            print("No employee records available.")
        else:
            print("\n--- All Employee Records ---")
            for emp in self.employees:
                print(emp)

    def search_by_id(self, emp_id):
        """Search employee by Employee ID"""
        for emp in self.employees:
            if emp.emp_id == emp_id:
                print("\n--- Employee Found ---")
                print(emp)
                return
        print("Employee not found.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python employee_system.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    system = EmployeeSystem(filename)

    
    system.display_all()

    
    emp_id = input("\nEnter Employee ID to search: ")
    system.search_by_id(emp_id)






EmployeeID,Name,Department,Salary
E101,Rahul Sharma,IT,60000
E102,Neha Patil,HR,50000
E103,Amit Kumar,Finance,70000
