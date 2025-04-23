class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1 
    @classmethod
    def display_count(cls):
        # Class method using cls to access class variable
        return f"Total objects created: {cls.count}"
    
    @classmethod
    def reset_count(cls):
        cls.count = 0
        return "Counter has been reset"
if __name__ == "__main__":
    print(Counter.display_count()) 
    
    c1 = Counter()
    print(Counter.display_count())  
    c2 = Counter()
    c3 = Counter()
    print(Counter.display_count()) 
    print(Counter.reset_count())
    print(Counter.display_count()) 
    c4 = Counter()
    print(Counter.display_count())  