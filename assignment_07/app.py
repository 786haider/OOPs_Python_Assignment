class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable (convention)
        self.__ssn = ssn        # Private variable (name mangling)
    
    def display_info(self):
        """Display all employee information including the private SSN"""
        return f"Name: {self.name}, Salary: {self._salary}, SSN: {self.__ssn}"

print("Creating an employee object...")
emp = Employee("John Doe", 75000, "123-45-6789")

# Accessing public variable
print("\nAccessing public variable:")
print(f"emp.name: {emp.name}")

# Accessing protected variable
print("\nAccessing protected variable:")
print(f"emp._salary: {emp._salary}")

# Attempting to access private variable
print("\nAttempting to access private variable:")
try:
    print(f"emp.__ssn: {emp.__ssn}")
except AttributeError as e:
    print(f"Error: {e}")

# Accessing private variable with name mangling
print("\nAccessing private variable with name mangling:")
print(f"emp._Employee__ssn: {emp._Employee__ssn}")

# Using class method to access all variables
print("\nAccessing all variables through class method:")
print(emp.display_info())