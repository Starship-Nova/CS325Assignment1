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
![Image of an animal](https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/2010-kodiak-bear-1.jpg/1200px-2010-kodiak-bear-1.jpg)