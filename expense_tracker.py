def load_expenses(filename):
    try:
        with open(filename,"r") as file:
            expenses = [line.strip() for line in file]
            return expenses

    except FileNotFoundError:
        return []

    except PermissionError:
        print("Error: Permission denied while reading the file.")
        return []

def save_expense(filename, record):
    try:
        with open(filename,"a") as file:
            file.write(record + "\n")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error occurred:",e)
        return []

def main():
    filename = "expenses.txt"
    expenses = load_expenses(filename)

    while True:
        print("\n==== DAILY EXPENSE TRACKER ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        if choice == 1:
            description = input("Enter expense description: ")
            try:
                amount = float(input("Enter expense amount: Rs."))
            except ValueError:
                print("Error: Amount must be a number.")
                continue
            record = f"Description: {description}, Amount: Rs. {amount:.2f}"

            save_expense(filename,record)
            expenses.append(record)
            print("Expense added successfully!")

        elif choice == 2:
            if not expenses:
                print("No records found.")
            else:
                print("\n----- EXPENSE RECORDS -----")

                for expense in expenses:
                    print(expense)

        elif choice == 3:
            print("Thank you for using Daily Expense Tracker!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()


       