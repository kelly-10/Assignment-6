def calculator():
    print("Simple Calculator")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid operation!"
        
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter numerical values.")

if __name__ == "__main__":
    calculator()
