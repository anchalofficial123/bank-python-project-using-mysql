from database import db_query, mydb

class Customer:
    def __init__(self, username, password, name, age, city, balance, account_number, status):
        self.username = username
        self.password = password
        self.name = name
        self.age = age
        self.city = city
        self.balance = balance
        self.account_number = account_number
        self.status = status

    def createuser(self):
        db_query(
            "INSERT INTO customers (username, password, name, age, city, balance, account_number, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (self.username, self.password, self.name, self.age, self.city, 0, self.account_number, 1)
        )
        mydb.commit()
