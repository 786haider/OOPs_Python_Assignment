class TemperatureConverter:
   
    @staticmethod
    def celsius_to_fahrenheit(celsius):
       
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def is_freezing(celsius):
        """
        Check if the temperature in Celsius is at or below freezing (0°C).
        
        Args:
            celsius (float): Temperature in Celsius
            
        Returns:
            bool: True if freezing, False otherwise
        """
        return celsius <= 0


# Test the TemperatureConverter class
if __name__ == "__main__":
    # Use the static methods directly from the class without creating an instance
    celsius = 25
    fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    
    fahrenheit = 98.6
    celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
    
    # Test multiple temperatures
    test_temps_c = [0, 100, -40, 37]
    for temp in test_temps_c:
        converted = TemperatureConverter.celsius_to_fahrenheit(temp)
        freezing = TemperatureConverter.is_freezing(temp)
        freezing_status = "freezing" if freezing else "not freezing"
        print(f"{temp}°C is {freezing_status} and equals {converted:.2f}°F")
    
    