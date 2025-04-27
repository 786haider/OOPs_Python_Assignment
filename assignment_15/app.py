class A:
    def show(self):
        return "Class A's show method"
    
    def __str__(self):
        return "Class A"


class B(A):
    def show(self):
        return "Class B's show method"
    
    def __str__(self):
        return "Class B"


class C(A):
    def show(self):
        return "Class C's show method"
    
    def __str__(self):
        return "Class C"


class D(B, C):
    def __str__(self):
        return "Class D"


# Example usage
if __name__ == "__main__":
    # Create an instance of D
    d = D()
    
    # Call the show method to see which one gets called
    print(d.show())  # This will call B's show method due to MRO
    
    # Print the MRO to understand why
    print("\nMethod Resolution Order for class D:")
    for cls in D.__mro__:
        print(f"- {cls.__name__}")
