# in python we have default sys module to read command line argumnets
#(default module comes with installation so no need to pip install)
import sys                    

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

x = float(sys.argv[1])        # we do not start with index [0] as that is assigned for command to run the program itself example aws s3 ls
operation = (sys.argv[2])     
y = float(sys.argv[3])        #convert to float as it reads comm. line args as strings so we need to convert them

if operation == 'add':
    result = add(x, y)
elif operation == 'subtract':
    result = subtract(x, y)
elif operation == 'multiply':
    result = multiply(x, y)
elif operation == 'divide':
    result = divide(x, y)
else:
    result = "Error! Unsupported operation."

print(result)