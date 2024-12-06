from register import SignUp, SignIn
from bank import Bank
from database import db_query, mydb  # Ensure database connection and query methods are defined here

def main_menu():
    print("\n==============================")
    print("Welcome to Mohit Banking Project!")
    print("==============================\n")
    while True:
        try:
            choice = int(input("1. SignUp\n"
                               "2. SignIn\n"
                               "Please choose an option: "))
            if choice == 1:
                SignUp()
            elif choice == 2:
                user = SignIn()
                return user
            else:
                print("Invalid choice. Please choose 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def banking_services(user):
    # Corrected the SQL query using %s for safe parameterized query
    account_data = db_query(
        "SELECT account_number FROM customers WHERE username = %s", (user,)
    )
    if not account_data:
        print("Account not found. Please contact customer support.")
        return

    account_number = account_data[0][0]
    bobj = Bank(user, account_number)

    while True:
        print(f"\nWelcome {user.capitalize()}! Choose Your Banking Service\n")
        try:
            service = int(input("1. Balance Enquiry\n"
                                "2. Cash Deposit\n"
                                "3. Cash Withdraw\n"
                                "4. Fund Transfer\n"
                                "5. Exit\n"
                                "Please choose an option: "))
            if service == 1:
                bobj.balanceequiry()
            elif service == 2:
                handle_deposit(bobj)
            elif service == 3:
                handle_withdraw(bobj)
            elif service == 4:
                handle_fund_transfer(bobj)
            elif service == 5:
                print("Thank you for using our banking services. Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def handle_deposit(bobj):
    while True:
        try:
            amount = int(input("Enter the amount to deposit: "))
            bobj.deposit(amount)
            mydb.commit()
            print("Deposit successful!")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def handle_withdraw(bobj):
    while True:
        try:
            amount = int(input("Enter the amount to withdraw: "))
            bobj.withdraw(amount)
            mydb.commit()
            print("Withdrawal successful!")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def handle_fund_transfer(bobj):
    while True:
        try:
            receiver = int(input("Enter the receiver's account number: "))
            amount = int(input("Enter the amount to transfer: "))
            bobj.fundtransfer(receiver, amount)
            mydb.commit()
            print("Fund transfer successful!")
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    user = main_menu()
    if user:
        banking_services(user)
