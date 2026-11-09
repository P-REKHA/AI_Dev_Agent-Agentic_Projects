
import json

HISTORY_FILE = "history.json"


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


def save_history(history):
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

        print("History saved successfully.")

    except OSError as error:
        print("Unable to save history:", error)


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
