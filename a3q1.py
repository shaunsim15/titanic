import psycopg2
from config import config # from config file, import config function

# Connect to the database
def connect():
    params = config() # params is a dict that looks something like: {'host': 'localhost', 'database': 'a3_q1', 'user': 'postgres', 'password': '56789'}
    print('Connecting to the postgreSQL database ...')
    connection = psycopg2.connect(**params)
    return connection

# Close the database connection. This function should always be called, even if an error occurs.
def closeConnect(connection, crsr):
    crsr.close()
    if connection is not None:
        connection.close()
        print('Database connection terminated')

# Retrieves and displays all records from the students table.
def getAllStudents(): 
    connection = None
    try: 
        connection = connect()
        crsr = connection.cursor()
        crsr.execute('SELECT * FROM students')
        print("Students:")
        for student in crsr.fetchall(): # Print each student record fetched by the cursor
            print(student)
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        closeConnect(connection, crsr)

# Inserts a new student record into the students table.
def addStudent(first_name, last_name, email, enrollment_date): 
    connection = None
    try: 
        connection = connect()
        crsr = connection.cursor()
        crsr.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES \
                    ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")
        print(f"{crsr.rowcount} row(s) inserted")
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        closeConnect(connection, crsr)

# Updates the email address for a student with the specified student_id.
def updateStudentEmail(student_id, new_email):
    connection = None
    try: 
        connection = connect()
        crsr = connection.cursor()
        crsr.execute(f"UPDATE students SET email='{new_email}'WHERE student_id={student_id}")
        print(f"{crsr.rowcount} row(s) updated")
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        closeConnect(connection, crsr)

# Deletes the record of the student with the specified student_id.
def deleteStudent(student_id): 
    connection = None
    try: 
        connection = connect()
        crsr = connection.cursor()
        crsr.execute(f"DELETE FROM students WHERE student_id={student_id}")
        print(f"{crsr.rowcount} row(s) deleted")
        connection.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        closeConnect(connection, crsr)


if __name__ == "__main__":
    # getAllStudents()
    # addStudent("Shaun", "Sim", "shaunsim@cmail.carleton.ca", "2024-02-14")
    # updateStudentEmail(1, 'a@b.com')
    deleteStudent(4)
