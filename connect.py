import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",passwd="anchal")
print(mydb,"connection established.......")
