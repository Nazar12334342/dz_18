import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="my_first_db"
)

cursor = connection.cursor()

cursor.execute("ALTER TABLE student MODIFY id INT PRIMARY KEY")

cursor.close()
connection.close()
