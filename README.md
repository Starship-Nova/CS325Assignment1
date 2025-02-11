# First assignment in CS325
CS325 is Software Engineering

## Example of Decorator Code
<code> 
def decorator_name(func):
    def wrapper(*args):
        result = func(*args)
        return result
    return wrapper

@decorator_name
def original_func(arg):
    return arg    
</code>

### Embedded Image
![Image of an animal](bear.jpg)