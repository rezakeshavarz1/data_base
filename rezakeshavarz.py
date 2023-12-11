import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
)
mycursor = mydb.cursor()

sql = "CREATE DATABASE IF NOT EXISTS SCHOOL"
mycursor.execute(sql)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="SCHOOL"
)
mycursor = mydb.cursor()

sql = """
        CREATE TABLE IF NOT EXISTS Students(
            s_id INT AUTO_INCREMENT,
            s_name VARCHAR(250),
            age INT,
            grade INT,
            c_id INT,
            PRIMARY KEY(s_id),
            FOREIGN KEY(c_id) REFERENCES Courses(c_id)
        );
    """
mycursor.execute(sql)

sql = """
        CREATE TABLE IF NOT EXISTS Courses(
            c_id INT AUTO_INCREMENT,
            c_name VARCHAR(250),
            PRIMARY KEY(c_id)
        );
    """
mycursor.execute(sql)

sql = "INSERT INTO Courses(c_name) VALUES ('Math')"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO Students(s_name, age, grade, c_id) VALUES ('John', 15, 9, 1)"
mycursor.execute(sql)
mydb.commit()

sql = "DELETE FROM Students WHERE s_name = 'John'"
mycursor.execute(sql)
mydb.commit()

sql = "DELETE FROM Courses WHERE c_id = 1"
mycursor.execute(sql)
mydb.commit()

sql = "SELECT * FROM Students"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

sql = "UPDATE Students SET grade = grade + 1"
mycursor.execute(sql)
mydb.commit()

sql = "SELECT * FROM Students WHERE s_name = 'John'"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

sql = "SELECT s_name FROM Students"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)

sql = "SELECT c_name FROM Courses"
mycursor.execute(sql)
result = mycursor.fetchall()
print(result)
