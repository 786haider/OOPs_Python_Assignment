class Engine:
    def __init__(self, horsepower, fuel_type):
        self.horsepower = horsepower
        self.fuel_type = fuel_type
        self.is_running = False
    
    def start(self):
        if not self.is_running:
            self.is_running = True
            return "Engine started! Vroom!"
        return "Engine is already running."
    
    def stop(self):
        if self.is_running:
            self.is_running = False
            return "Engine stopped."
        return "Engine is already off."
    
    def get_specs(self):
        return f"{self.horsepower} HP, {self.fuel_type} engine"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has-an Engine
    
    def start_car(self):
        return f"{self.make} {self.model}: {self.engine.start()}"
    
    def stop_car(self):
        return f"{self.make} {self.model}: {self.engine.stop()}"
    
    def car_details(self):
        return f"{self.make} {self.model} with {self.engine.get_specs()}"

# Example usage
if __name__ == "__main__":
    # Create an Engine object
    my_engine = Engine(300, "Gasoline")
    
    # Pass the Engine object to a Car object (composition)
    my_car = Car("Toyota", "Supra", my_engine)
    
    # Access Engine methods through the Car object
    print(my_car.start_car()) 
    print(my_car.car_details())
    print(my_car.stop_car())  