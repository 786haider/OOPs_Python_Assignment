class MathUtils:
    @staticmethod
    def add(a, b):
        """
        Static method that returns the sum of two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        return a + b
if __name__ == "__main__":
    # We can call the static method directly from the class
    # without creating an instance
    result = MathUtils.add(5, 3)
    print(f"5 + 3 = {result}")
    