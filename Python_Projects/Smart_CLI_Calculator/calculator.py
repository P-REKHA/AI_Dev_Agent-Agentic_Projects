
import json

# ==========================================
#       SMART PYTHON CALCULATOR
# ==========================================

HISTORY_FILE = "history.json"


# Arithmetic functions

def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


def modulus(first_number, second_number):
    return first_number % second_number


def exponentiation(first_number, second_number):
    return first_number ** second_number


def floor_division(first_number, second_number):
    return first_number // second_number


# Load history from JSON

def load_history():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("History must contain a JSON list.")

        print("Previous history loaded successfully.")
        return data, True

    except FileNotFoundError:
        print("No previous history found. Starting fresh.")
        return [], True

    except json.JSONDecodeError:
        print("Error: History file contains invalid JSON.")
        print("History will not be overwritten automatically.")
        return [], False

    except (OSError, ValueError) as error:
        print("Unable to load history:", error)
        return [], False


# Save history to JSON

def save_history(history):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

        print("History saved successfully.")

    except OSError as error:
        print("Unable to save history:", error)


# Display history

def view_history(history):

    if not history:
        print("\nNo calculation history available.")

    else:
        print("\n========== CALCULATION HISTORY ==========")

        for index, record in enumerate(history, start=1):
            print(
                f"{index}. {record['first_number']} "
                f"{record['symbol']} {record['second_number']} "
                f"= {record['result']}"
            )

        print("=========================================")


# Load previous history when program starts

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

    if choice == "9":
        print("Thank you for using the calculator!")
        break

    elif choice == "8":
        view_history(history)

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

            print(f"\n{first_number} {symbol} {second_number} = {result}")

            # Create history record

            record = {
                "operation": operation,
                "symbol": symbol,
                "first_number": first_number,
                "second_number": second_number,
                "result": result
            }

            history.append(record)

            # Save history after successful calculation

            if storage_available:
                save_history(history)
            else:
                print("History is in memory only. Fix the JSON file to save it.")

        except ValueError:
            print("Error: Please enter valid numeric values.")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")

    else:
        print("Invalid choice! Please select between 1 and 9.")
