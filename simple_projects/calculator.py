import math


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


def exponentiate(x, y):
    return x ** y


def square_root(x):
    if x < 0:
        return "Error! Cannot take square root of a negative number."
    return math.sqrt(x)


def calculator():
    global result
    history = []

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponentiate")
    print("6. Square Root")
    print("7. View History")
    print("8. Clear History")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/8) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6'):
            try:
                if choice == '6':  # Square root takes only one input
                    num1 = float(input("Enter number: "))
                    result = square_root(num1)
                    print(f"√{num1} = {result}")
                    history.append(f"√{num1} = {result}")
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))

                    if choice == '1':
                        result = add(num1, num2)
                        print(f"{num1} + {num2} = {result}")
                    elif choice == '2':
                        result = subtract(num1, num2)
                        print(f"{num1} - {num2} = {result}")
                    elif choice == '3':
                        result = multiply(num1, num2)
                        print(f"{num1} * {num2} = {result}")
                    elif choice == '4':
                        result = divide(num1, num2)
                        print(f"{num1} / {num2} = {result}")
                    elif choice == '5':
                        result = exponentiate(num1, num2)
                        print(f"{num1} ^ {num2} = {result}")

                    history.append(
                        f"{num1} {'+' if choice == '1' else '-' if choice == '2' else '*' if choice == '3' else '/' if choice == '4' else '^'} {num2} = {result}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == '7':
            print("Calculation History:")
            for entry in history:
                print(entry)
        elif choice == '8':
            history.clear()
            print("History cleared.")
        else:
            print("Invalid choice. Please select a valid operation.")


if __name__ == "__main__":
    calculator()
