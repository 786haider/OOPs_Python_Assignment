class Logger:
    def __init__(self, name="Default"):
        """
        Constructor method that runs when an object is created.
        
        Args:
            name: An identifier for this logger instance
        """
        self.name = name
        print(f"Logger '{self.name}' has been created.")
    
    def __del__(self):
        """
        Destructor method that runs when an object is destroyed.
        """
        print(f"Logger '{self.name}' is being destroyed.")

if __name__ == "__main__":
    print("Creating first logger...")
    logger1 = Logger("MainLogger")
    
    print("\nCreating second logger...")
    logger2 = Logger("DebugLogger")
    
    print("\nDeleting first logger...")
    del logger1
    
    print("\nProgram ending - second logger will be automatically destroyed")
   