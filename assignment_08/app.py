class Person:
    def __init__(self, name):
        """
        Constructor for the Person class.
        
        Args:
            name: The person's name
        """
        self.name = name
        print(f"Person constructor called with name: {self.name}")
    
    def introduce(self):
        """Simple introduction method"""
        return f"My name is {self.name}"


class Teacher(Person):
    def __init__(self, name, subject):
        """
        Constructor for the Teacher class.
        
        Args:
            name: The teacher's name
            subject: The subject they teach
        """
        # Call the parent class constructor using super()
        super().__init__(name)
        
        # Add Teacher-specific attributes
        self.subject = subject
        print(f"Teacher constructor called with subject: {self.subject}")
    
    def introduce(self):
        """Override the introduce method to include subject"""
        base_intro = super().introduce()
        return f"{base_intro} and I teach {self.subject}"



if __name__ == "__main__":
    # Create a Person object
    print("Creating a Person:")
    person = Person("Alice")
    print(person.introduce())
    print()
    
    # Create a Teacher object
    print("Creating a Teacher:")
    teacher = Teacher("Mr. Smith", "Mathematics")
    print(teacher.introduce())
    
    # Demonstrate inheritance
    print("\nDemonstrating inheritance:")
    print(f"Is teacher a Person? {isinstance(teacher, Person)}")
    print(f"Is teacher a Teacher? {isinstance(teacher, Teacher)}")