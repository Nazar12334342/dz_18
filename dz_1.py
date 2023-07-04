import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE my_first_db")

cursor.close()
connection.close()
