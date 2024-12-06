from database import db_query
import random
from customer import Customer
from bank import Bank
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def SignUp():
    while True:
        username = input("Create Username: ")
        temp = db_query("SELECT username FROM customers WHERE username = %s;", (username,))
        if temp:
            print("Username Already Exists. Please try a different username.")
        else:
            print("Username is Available. Please Proceed.")
            break

    password = input("Enter Your Password: ")
    hashed_password = hash_password(password)
    
    name = input("Enter Your Name: ")
    while True:
        try:
            age = int(input("Enter Your Age: "))
            if age < 18:
                print("You must be at least 18 years old to create an account.")
                return
            break
        except ValueError:
            print("Please enter a valid age.")

    city = input("Enter Your City: ")

    while True:
        account_number = random.randint(10000000, 99999999)
        temp = db_query("SELECT account_number FROM customers WHERE account_number = %s;", (account_number,))
        if not temp:
            print("Your Account Number:", account_number)
            break

    # Initialize account balance and status
    balance = 0.0
    status = "active"

    cobj = Customer(username, hashed_password, name, age, city, balance, account_number, status)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
    print("Sign-Up Completed Successfully!")

def SignIn():
    username = input("Enter Username: ")
    temp = db_query("SELECT username FROM customers WHERE username = %s;", (username,))
    if not temp:
        print("Incorrect Username. Please try again.")
        return None

    while True:
        password = input(f"Welcome {username.capitalize()}! Enter Password: ")
        hashed_password = hash_password(password)
        temp = db_query("SELECT password FROM customers WHERE username = %s;", (username,))
        if temp and temp[0][0] == hashed_password:
            print("Sign In Successful!")
            return username
        else:
            print("Incorrect Password. Please try again.")
