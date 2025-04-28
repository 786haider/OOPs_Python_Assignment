class Product:
    def __init__(self, name, price):
        self.name = name
        # I'll make price private with underscore
        self._price = price
        
    # Property decorator to get the price
    @property
    def price(self):
        # Adding a print statement that a student might use for debugging
        # print(f"Getting price for {self.name}")
        return self._price
    
    # Setter for updating the price
    @price.setter
    def price(self, new_price):
        # Some basic validation a student might include
        if new_price < 0:
            # This kind of print during validation is common in student code
            print("Price can't be negative!")
            return
        
        if not isinstance(new_price, (int, float)):
            print("Price must be a number")
            return
            
        # Update the price if all checks pass
        print(f"Changing price from ${self._price} to ${new_price}")
        self._price = new_price
    
    # Deleter for removing the price attribute
    @price.deleter
    def price(self):
        print(f"Deleting price for {self.name}")
        del self._price
        
# Test the class with some examples
if __name__ == "__main__":
    # Create a new product
    laptop = Product("Laptop", 999.99)
    
    # Get the price using the property
    print(f"The price of the {laptop.name} is ${laptop.price}")
    
    # Update the price using the setter
    laptop.price = 899.99
    print(f"After discount: ${laptop.price}")
    
    # Try setting an invalid price
    laptop.price = -50
    
    # Delete the price
    del laptop.price
    