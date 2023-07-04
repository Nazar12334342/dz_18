import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="my_first_db"
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE student (id INT, name VARCHAR(255))")

cursor.close()
connection.close()
