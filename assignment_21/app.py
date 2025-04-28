class Countdown:
    """
    A countdown iterator that counts from a start number down to 0.
    """
    def __init__(self, start):
        """
        Initialize the countdown with a starting number.
        
        Args:
            start: The number to start counting down from
        """
        self.start = start
        self.current = start
    
    def __iter__(self):
        """
        Return the iterator object itself.
        This is called when creating an iterator from the iterable.
        """
        self.current = self.start  # Reset the counter when starting iteration
        return self
    
    def __next__(self):
        """
        Return the next value in the countdown sequence.
        Raises StopIteration when the countdown is complete.
        """
        if self.current < 0:
            raise StopIteration
        
        value = self.current
        self.current -= 1
        return value


# Example usage
countdown = Countdown(5)
print("Example 1: Basic for loop")
for num in countdown:
    print(num)

print("\nExample 2: Converting to list")
countdown = Countdown(3)
countdown_list = list(countdown)
print(countdown_list)

print("\nExample 3: Multiple iterations")
countdown = Countdown(2)
print("First iteration:", end=" ")
for num in countdown:
    print(num, end=" ")
    
print("\nSecond iteration:", end=" ")
for num in countdown:
    print(num, end=" ")