def calculator():
    while True:
        print("\t  1 for Addition Operator")
        print("\t  2 for Subtraction Operator")
        print("\t  3 for Multiplication Operator")
        print("\t  4 for Division Operator")
        print("\t  5 for Remainder Operator")
        print("\t  6 for Power Operator")

        try:
            operation = int(input("Enter a number to select an operation (1-6): "))
            if 1 <= operation <= 6:
                print(f"You selected option {operation}.")
                break  # Exit the loop if the input is valid
            else:
                print("Invalid input! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    while True:
        try:
            m = float(input("Enter your first value :"))
            n = float(input("Enter your second value:"))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    match operation:
        case 1:
            return f"Result: {m + n}"
        case 2:
            return f"Result: {m - n}"
        case 3:
            return f"Result: {m * n}"
        case 4:
            if n != 0:
                return f"Result: {m / n}"
            else:
                return "Error: Division by zero is not allowed."
        case 5:
            return f"Result: {m % n}"
        case 6:
            return f"Result: {m ** n}"
        case _:
            return "Enter a valid input"


while True:
    result = calculator()
    print(result)  # Print the result of the operation

    while True:
        user = input("If you want to perform again, type (YES/NO): ").strip().upper()
        if user in ["YES", "NO"]:
            break  # Exit loop if input is valid
        else:
            print("Invalid input! Please enter either YES or NO.")

    if user == "NO":
        print("Thank you for using the application!")
        break

