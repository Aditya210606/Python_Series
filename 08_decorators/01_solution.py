import time 

def timer(func):
    def wrapper(*args, **kwargs):   #  args and kwargs means input from the users 
       start = time.time()
       result =  func(*args, **kwargs)
       end = time.time()
       print(f"{func.__name__} ran in {end-start} time")
       return result 
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

example_function(2)
