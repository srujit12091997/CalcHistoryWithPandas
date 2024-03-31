from dotenv import load_dotenv
import os
import logging.config
from app.core.calculator import Calculator
from app.core.calculator import AddStrategy, SubtractStrategy, MultiplyStrategy, DivideStrategy  # Import the strategy classes

def print_menu():
    print("\n--- Calculator Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Clear History")
    print("7. Quit")

def get_numeric_input(prompt):
    """Get numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    # Load environment variables from .env file
    load_dotenv()

    # Configure logging
    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)

    # Get configuration from environment variables
    log_level = os.getenv('LOG_LEVEL', 'INFO')
    history_file_path = os.getenv('HISTORY_FILE_PATH', 'data/history.csv')

    # Set logging level
    logging.basicConfig(level=log_level)

    # Instantiate calculator with history file path
    calculator = Calculator(history_file_path)

    # Main REPL loop
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3', '4']:
            a = get_numeric_input("Enter first number: ")
            b = get_numeric_input("Enter second number: ")

            # Set strategy based on user choice
            if choice == '1':
                calculator.set_strategy(AddStrategy())
            elif choice == '2':
                calculator.set_strategy(SubtractStrategy())
            elif choice == '3':
                calculator.set_strategy(MultiplyStrategy())
            elif choice == '4':
                calculator.set_strategy(DivideStrategy())
            
            # Perform the calculation
            result = calculator.calculate(a, b)
            print("Result:", result)
            
            # Update history
            calculator.update_history(a, b, choice, result)
        elif choice == '5':
            print("\n--- Calculation History ---")
            print(calculator.history_df)
        elif choice == '6':
            calculator.clear_history()
            print("History cleared successfully.")
        elif choice == '7':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid choice. Please select a number from the menu.")

if __name__ == "__main__":
    main()
