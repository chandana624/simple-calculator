"""
Simple Calculator
A basic console-based calculator that performs addition, subtraction,
multiplication, and division.

Author: Chandana T
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def main():
    print("=== Simple Calculator ===")
    print("Operations: + (add), - (subtract), * (multiply), / (divide)")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operator. Please use +, -, * or /")
                continue

            print(f"Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

        again = input("\nDo you want to calculate again? (yes/no): ")
        if again.lower() != "yes":
            print("Thank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
