import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="my_first_db"
)

cursor = connection.cursor()

student_data = (1, 'John')
student_query = "INSERT INTO student (id, name) VALUES (%s, %s)"
cursor.execute(student_query, student_data)

employee_data = (1, 'John', 10000)
employee_query = "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)"
cursor.execute(employee_query, employee_data)

connection.commit()

cursor.close()
connection.close()
