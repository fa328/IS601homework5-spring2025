'''Main.py function'''
import sys
from decimal import Decimal, InvalidOperation
from calculator import Calculator

from app import App


def calculate_and_print(a, b, operation_name):
    '''calculate and print function'''
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    # Unified error handling for decimal conversion
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name) # Use get to handle unknown operations
        if result:
            print(f"The result of {a} {operation_name} {b} "
                   f"is equal to {result(a_decimal, b_decimal)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except (ValueError, KeyError) as e: # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    '''Main function'''
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation)

# You must put this in your main.py
# because this forces the program to start when you run it from the command line.
    app = App()
    app.start()

if __name__ == '__main__':
    main()
