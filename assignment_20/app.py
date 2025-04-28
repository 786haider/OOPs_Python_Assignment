class InvalidAgeError(Exception):
    """Custom exception raised when age is below 18."""
    def __init__(self, age, message="Age must be at least 18 years"):
        self.age = age
        self.message = message
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.message}. You provided: {self.age}"

def check_age(age):
    """
    Check if the age is valid (18 or above).
    
    Args:
        age: The age to check
        
    Raises:
        InvalidAgeError: If age is less than 18
    """
    if age < 18:
        raise InvalidAgeError(age)
    else:
        return f"Age validation successful. Age: {age}"


try:
    # Test with an invalid age
    print(check_age(16))
except InvalidAgeError as error:
    print(f"Error caught: {error}")

try:
    # Test with a valid age
    print(check_age(21))
except InvalidAgeError as error:
    print(f"Error caught: {error}")