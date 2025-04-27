class Employee:
    def __init__(self, name, employee_id, role):
        self.name = name
        self.employee_id = employee_id
        self.role = role
    
    def get_details(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Role: {self.role}"
    
    def work(self):
        return f"{self.name} is working on tasks for their role as {self.role}."


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store references to existing Employee objects
    
    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)
            return f"Added {employee.name} to {self.name} department."
        return f"{employee.name} is already in the {self.name} department."
    
    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            return f"Removed {employee.name} from {self.name} department."
        return f"{employee.name} is not in the {self.name} department."
    
    def list_employees(self):
        if not self.employees:
            return f"No employees in the {self.name} department."
        
        result = f"Employees in {self.name} department:"
        for employee in self.employees:
            result += f"\n- {employee.get_details()}"
        return result


# Example usage
if __name__ == "__main__":
    # Create Employee objects that can exist independently
    employee1 = Employee("Alice Johnson", "E001", "Software Developer")
    employee2 = Employee("Bob Smith", "E002", "Project Manager")
    employee3 = Employee("Charlie Davis", "E003", "UX Designer")
    
    # Create a Department
    tech_department = Department("Technology")
    
    # Add employees to the department (aggregation)
    print(tech_department.add_employee(employee1))
    print(tech_department.add_employee(employee2))
    
    # List all employees in the department
    print(tech_department.list_employees())
    
    # Employee objects can exist independently of the department
    print(employee3.get_details())  # This employee isn't in any department yet
    
    # Remove an employee from the department
    print(tech_department.remove_employee(employee1))
    
    # The employee still exists even after removal from department
    print(employee1.work())  # Employee object continues to exist