def add(x,y):
    return x + y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def div(x,y):
    return x/y

operation = input("Select operation: add, sub, mult, or div ")
num1 = input("select num: ")
num2 = input("select another num: ")

if operation == "add":
    print(add(int(num1),int(num2)))
elif operation == "sub":
    print(sub(int(num1),int(num2)))
elif operation == "mult":
    print(mult(int(num1),int(num2)))
elif operation == "div":
    print(div(int(num1),int(num2)))
else:
    print("error operation")