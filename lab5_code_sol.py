# Programmers:  [your name here]
# Course:  CS151, [Instructors name here]
# Due Date: [date assignment is due]
# Programming Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Display the purpose of the program
INITIAL_BALANCE = 1000
SENTINEL = 'E'

def display_menu():
    print("\nPlease select an option:"
            "\n\t D - Deposit"
            "\n\t W - Withdraw"
            "\n\t V - View Balance"
            "\n\t E - Exit")

def read_amount(prompt):
    amount = input(prompt)
    
    if not amount.isdigit() or int(amount) < 0:
        print('This is invalid amount')
        return 0
    else:
        return int(amount)

def deposit(balance):
    amount = read_amount('Enter the deposit amount: ')
    return balance + amount

def main():
    
    print("Welcome to the ATM program! This program allows you to interact with your account balance.")

    # Initialize variables
    
    current_balance = INITIAL_BALANCE
    choice = ''

    # Start the loop until the user decides to exit
    while choice.upper() != SENTINEL:
        # Display the menu
        display_menu()

        choice = input("Your choice: ").strip().upper()

        # Process the choice
        if choice == 'D':
            current_balance = deposit(current_balance)

        elif choice == 'V':
            # Clear the screen and show the balance
            print(f"Your current balance is ${current_balance:.2f}.")

        elif choice == 'W':
            withdraw_amount = read_amount('Enter the withdraw amount: ')
            current_balance -= withdraw_amount
            
            # Warning if the balance is negative
            if current_balance < 0:
                print("❕ Warning: You have a negative balance. You will be charged 5% interest.")

        elif choice == 'E':
            print("Thank you for using the ATM program. Goodbye!")
        else:
            print("Error: Invalid choice. Please enter D, W, V, or E.")

    print("ATM program has ended.")
    
main()