

# Initialize balance
balance = 0

# Function to credit amount
def credit(amount):
    global balance
    if amount <= 0:
        print("Please enter a positive amount.")
    else:
        balance += amount
        print(f"{amount} credited to your account.")

# Function to debit amount
def debit(amount):
    global balance
    if amount <= 0:
        print("Please enter a positive amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"{amount} debited from your account.")

# Function to show balance
def show_balance():
    print(f"Your current balance is: {balance}")

# Function to display ATM menu
def atm_menu():
    print("\nATM Menu:")
    print("1. Credit")
    print("2. Debit")
    print("3. Balance")
    print("4. Exit")

# Main ATM 
def atm():
    while True:
        atm_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to credit: "))
            credit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to debit: "))
            debit(amount)
        elif choice == '3':
            show_balance()
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the ATM program
atm()
