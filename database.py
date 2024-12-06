import sys
sys.stdout.reconfigure(encoding='utf-8')  # Set UTF-8 encoding for output

import mysql.connector as sql

# MySQL Connection
try:
    mydb = sql.connect(
        host="localhost",
        user="root",  # Apna MySQL username daalein
        passwd="anchal",  # Apna MySQL password daalein
        database="banking_system"  # Apna database ka naam
    )
    print("MySQL connection successful!")
except sql.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

cursor = mydb.cursor()
def db_query(query,params=None):
    try:
        cursor.execute(query,params)
        result = cursor.fetchall()
        return result
    except sql.Error as e:
        print(f"Error executing query: {e}")

# Customers Table Creation Function
def create_customer_table():
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name VARCHAR(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL DEFAULT 0,  -- Default value for balance
                account_number INTEGER NOT NULL,
                status BOOLEAN NOT NULL DEFAULT TRUE -- Default value for status
            )
        ''')
        mydb.commit()
        print("Customers table created successfully!")
    except sql.Error as e:
        print(f"Error creating table: {e}")

# Main Function
if __name__ == "__main__":
    create_customer_table()
