def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name="World"):
    return f"Hello, {name}!"

# Test the decorated function
if __name__ == "__main__":
    # This will print "Function is being called" before executing say_hello
    print(say_hello())
    
    # The decorator works with arguments too
    print(say_hello("Python"))