import time

def cache(func):
    cache_value = {}  # why dict taken because it is easy to access
    print(cache_value)  
    def wrapper(*args):
       if args in cache_value:
           return cache_value[args]
       result =  func(*args)
       cache_value[args] = result
       return result
    return wrapper




@cache
def long_running_function(a,b):
    time.sleep(4)
    return a + b 

print(long_running_function(3, 2))
print(long_running_function(3, 2))


