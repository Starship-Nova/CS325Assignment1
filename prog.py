def my_decorator(func):
    def wrapper(*args):
        print("before calling the function")
        result = func(*args)
        print("after calling the function", result)
        return result
    return wrapper

@my_decorator
def greet(name):
    print("Inside the function" "hello" + name + "!")

def break_add(func):
    def wrapper(*args):
        print("this should make the result incorrect")
        sum = func(*args)
        print(sum * sum)
        print("that should be the wrong result")
        return sum * sum
    return wrapper

@break_add
def add(num1, num2):
    return num1 + num2

greet ("alice")

add (2,2)