class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand
        
    # Public method
    def start(self):
        return f"{self.brand} engine started. Vroom vroom!"
    
# Instantiate the class
my_car = Car("Toyota")

# Access the public variable from outside the class
print(f"Car brand: {my_car.brand}")

# Modify the public variable from outside the class
my_car.brand = "Honda"
print(f"Updated car brand: {my_car.brand}")

# Access the public method from outside the class
print(my_car.start())

# Create another car instance
luxury_car = Car("Mercedes")
print(f"Second car brand: {luxury_car.brand}")
print(luxury_car.start())