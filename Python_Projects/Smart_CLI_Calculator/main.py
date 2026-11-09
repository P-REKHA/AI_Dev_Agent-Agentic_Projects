
# ==========================================
#       SMART PYTHON CALCULATOR
# ==========================================

# Import arithmetic functions
from operations import (
    add,
    subtract,
    multiply,
    divide,
    modulus,
    exponentiation,
    floor_division
)

# Import history functions
from history_manager import (
    load_history,
    save_history,
    view_history
)


def main():

    # Load previous calculation history
    history, storage_available = load_history()

    # Main calculator loop
    while True:

        print("\n================================")
        print("       SMART PYTHON CALCULATOR")
        print("================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Floor Division")
        print("8. View History")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        # Exit
        if choice == "9":
            print("Thank you for using the calculator!")
            break

        # View calculation history
        elif choice == "8":
            view_history(history)

        # Perform arithmetic operations
        elif choice in ("1", "2", "3", "4", "5", "6", "7"):

            try:

                first_number = float(input("Enter first number: "))
                second_number = float(input("Enter second number: "))

                if choice == "1":
                    operation = "Addition"
                    symbol = "+"
                    result = add(first_number, second_number)

                elif choice == "2":
                    operation = "Subtraction"
                    symbol = "-"
                    result = subtract(first_number, second_number)

                elif choice == "3":
                    operation = "Multiplication"
                    symbol = "*"
                    result = multiply(first_number, second_number)

                elif choice == "4":
                    operation = "Division"
                    symbol = "/"
                    result = divide(first_number, second_number)

                elif choice == "5":
                    operation = "Modulus"
                    symbol = "%"
                    result = modulus(first_number, second_number)

                elif choice == "6":
                    operation = "Exponentiation"
                    symbol = "**"
                    result = exponentiation(first_number, second_number)

                elif choice == "7":
                    operation = "Floor Division"
                    symbol = "//"
                    result = floor_division(first_number, second_number)

                # Display result
                print(f"\n{first_number} {symbol} {second_number} = {result}")

                # Create history record
                record = {
                    "operation": operation,
                    "symbol": symbol,
                    "first_number": first_number,
                    "second_number": second_number,
                    "result": result
                }

                # Add record to history
                history.append(record)

                # Save history
                if storage_available:
                    save_history(history)
                else:
                    print(
                        "History is in memory only. "
                        "Fix the JSON file to save it."
                    )

            except ValueError:
                print("Error: Please enter valid numeric values.")

            except ZeroDivisionError:
                print("Error: Cannot divide by zero!")

        else:
            print("Invalid choice! Please select between 1 and 9.")


# Program entry point
if __name__ == "__main__":
    main()
