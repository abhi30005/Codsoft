def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Syntax Error..!")
    return x / y
def calculator():
    while True:
        print("=== Menu ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit.")
        choice = input("Enter choice: ")

        if choice == '5':
            print("Thank You..!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Syntax Error..!!")
                continue

            if choice == '1':
                result=add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result=subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result=multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                except ZeroDivisionError as e:
                    print(e)
        else:
            print("Invalid choice..!\n Please enter right choice from the list..")


if __name__ == "__main__":
    calculator()
