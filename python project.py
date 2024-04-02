def add(x, y):
    """Addition Function"""
    return x + y

def subtract(x, y):
    """Subtraction Function"""
    return x - y

def multiply(x, y):
    """Multiplication Function"""
    return x * y

def divide(x, y):
    """Division Function"""
    if y == 0:
        return "Error! Division by zero!"
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input")
        return

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))

calculator()
