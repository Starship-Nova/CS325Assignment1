def my_decorator(func):
    def wrapper(*args):
        print("this is the second file")
        result = func(*args)
        print("so some differences", result)
        return result
    return wrapper

@my_decorator
def greet(name):
    print("Inside the function" "hello" + name + "!")

def break_add(func):
    def wrapper(*args):
        print("will be printed")
        sum = func(*args)
        print(sum * sum)
        print("still the wrong result though")
        return sum * sum
    return wrapper

@break_add
def add(num1, num2):
    return num1 + num2

greet ("alice")

add (2,2)