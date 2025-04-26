class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says: Woof! Woof!")
    
    def get_info(self):
        return f"{self.name} is a {self.breed}"

if __name__ == "__main__":
    dog1 = Dog("Buddy", "Golden Retriever")
    dog2 = Dog("Max", "German Shepherd")
    
    # Call the instance methods
    dog1.bark()
    dog2.bark()
    
    # Display dog information
    print(dog1.get_info())
    print(dog2.get_info())
    
    # Demonstrate that each dog instance has its own state
    print(f"Dog 1 name: {dog1.name}, breed: {dog1.breed}")
    print(f"Dog 2 name: {dog2.name}, breed: {dog2.breed}")