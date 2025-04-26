class Book:
    total_books = 0
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        # Call the class method to increment the book count
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        """
        Class method to increment the total book count.
        Uses cls to access the class variable.
        """
        cls.total_books += 1
        return cls.total_books
    
    @classmethod
    def get_total_books(cls):
        """
        Class method to get the current total number of books.
        """
        return cls.total_books
    
    def get_info(self):
        """
        Instance method to get information about the book.
        """
        return f"'{self.title}' by {self.author}"


# Test the Book class
if __name__ == "__main__":
    # Print initial book count
    print(f"Initial total books: {Book.get_total_books()}")
    
    # Create some books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    print(f"After adding one book: {Book.get_total_books()}")
    
    book2 = Book("To Kill a Mockingbird", "Harper Lee")
    book3 = Book("1984", "George Orwell")
    print(f"After adding more books: {Book.get_total_books()}")
    
    # Display book information
    print(f"Book 1: {book1.get_info()}")
    print(f"Book 2: {book2.get_info()}")
    print(f"Book 3: {book3.get_info()}")
    
    # Demonstrate that the class variable is shared
    print(f"Book.total_books: {Book.total_books}")
    print(f"book1.total_books: {book1.total_books}")
    print(f"book2.total_books: {book2.total_books}")
    
    # Manually increment the book count
    Book.increment_book_count()
    print(f"After manual increment: {Book.get_total_books()}")