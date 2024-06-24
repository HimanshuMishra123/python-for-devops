def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


print(add(5,10))
print(subtract(5,10))
print(multiply(5,10))
print(divide(5,10))
