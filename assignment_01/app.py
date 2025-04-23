class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Student Marks: {self.marks}")
        
if __name__ == "__main__":
    # Create student objects
    student1 = Student("Alice", 95)
    student2 = Student("Bob", 87)
    print("Student 1 Details:")
    student1.display()
    
    print("\nStudent 2 Details:")
    student2.display()