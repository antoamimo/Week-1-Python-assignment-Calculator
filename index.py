# A simple Python program for a basic calculator.

def calculator():
    """
    This function prompts the user for two numbers and an operation,
    then performs the calculation and prints the result.
    """
    try:
        # Step 1: Ask the user to input two numbers.
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Step 2: Ask the user to input a mathematical operation.
        operation = input("Enter an operation (+, -, *, /): ")

        result = 0  # Initialize result variable

        # Step 3: Perform the operation based on the user's input.
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Handle division by zero to prevent an error.
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return  # Exit the function if division by zero occurs
            result = num1 / num2
        else:
            # Handle cases where the user enters an invalid operation.
            print("Error: Invalid operation. Please use +, -, *, or /.")
            return

        # Step 4: Print the result in the specified format.
        print(f"{num1} {operation} {num2} = {result}")

    except ValueError:
        # Handle cases where the user enters non-numeric input for the numbers.
        print("Error: Invalid input. Please enter valid numbers.")

# Run the calculator program.
calculator()