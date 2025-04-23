class Bank:
    bank_name = "Global Banking Corporation"

    def __init__(self, branch_location, manager):
        # Instance variables unique to each instance
        self.branch_location = branch_location
        self.manager = manager
    
    def display_info(self):
        return f"Branch: {self.branch_location}, Manager: {self.manager}, Bank: {self.bank_name}"
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        return f"Bank name changed to {cls.bank_name}"

# Create two bank instances
branch1 = Bank("Downtown", "Alice Johnson")
branch2 = Bank("Uptown", "Bob Smith")

# Display initial information
print("Initial state:")
print(branch1.display_info())
print(branch2.display_info())
print(f"Accessing class variable directly: {Bank.bank_name}")

# Change the bank name using the class method
print("\nChanging bank name...")
Bank.change_bank_name("Unified Financial Services")

# Show that the change affects all instances
print("\nAfter name change:")
print(branch1.display_info())
print(branch2.display_info())
print(f"Accessing class variable directly: {Bank.bank_name}")

# Can also call the class method from an instance 
print("\nChanging name again through instance...")
branch1.change_bank_name("City Trust Bank")

# Show that it still affects all instances
print("\nAfter second name change:")
print(branch1.display_info())
print(branch2.display_info())
print(f"Accessing class variable directly: {Bank.bank_name}")