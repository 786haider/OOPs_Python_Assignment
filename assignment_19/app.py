class Multiplier:
    def __init__(self, factor):
        self.factor = factor
        
    def __call__(self, number):
        # I'm going to multiply the input by our factor
        result = number * self.factor
        print(f"Multiplying {number} by {self.factor}")
        return result

# Let's test this out
if __name__ == "__main__":
    # Create a multiplier that doubles values
    doubler = Multiplier(2)
    print("Is doubler callable?", callable(doubler))  # Should be True because we defined __call__
    
    result = doubler(5)
    print(f"Double of 5 is: {result}")
    
    tripler = Multiplier(3)
    print(f"Triple of 10 is: {tripler(10)}")
    
    # Maybe we can do some more complex stuff
    numbers = [1, 2, 3, 4, 5]
    # Use the multiplier with a list comprehension
    doubled_list = [doubler(num) for num in numbers]
    print(f"Original list: {numbers}")
    print(f"Doubled list: {doubled_list}")
    