import psycopg2
import sys

# Connect to the A3 database
def connect():
    con = psycopg2.connect(
        dbname="A3",
        user="postgres",
        password="0204",
        host="localhost",
        port="5432"
    ) 
    return (con, con.cursor())

# Global connection and cursor objects
(connection, cursor) = connect()

# Read
def getAllStudents():
    cursor.execute(f"SELECT * FROM Students")

    head = f"All Students:\n{"id": ^5}|{"first_name": ^12}|{"last_name": ^12}|{"email": ^30}|{"enrollment_date": ^18}"
    print(head)
    for i in range(80):
        print("-", end="")
    print()
    
    for row in cursor.fetchall():
        print(f"{row[0]: ^5}|{row[1]: <12}|{row[2]: <12}|{row[3]: <30}|{str(row[4]): ^18}")
    print()

# Create
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute(f"INSERT INTO Students (first_name, last_name, email, enrollment_date) \
                    VALUES('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")

    print(f"Added student: {first_name} {last_name}")
    print()

# Update
def updateStudentEmail(student_id, new_email):
    cursor.execute(f"UPDATE Students \
                    SET email = '{new_email}' \
                    WHERE student_id = {student_id}")
    
    print(f"Changed the email of student with ID {student_id} to: {new_email}")
    print()

# Delete
def deleteStudent(student_id):
    cursor.execute(f"DELETE FROM Students \
                    WHERE student_id = {student_id}")
    
    print(f"Deleted student with ID {student_id}")
    print()

def main():
    action = None
    if len(sys.argv) > 1:
        action = sys.argv[1]

    # Read
    if not action or action.lower() == "r" or action.lower() == "read":
        getAllStudents()

    # Create
    if not action or action.lower() == "c" or action.lower() == "create":
        if len(sys.argv) < 6:
            print("Not enough arguments. Please provide first name, last name, email, and enrollment date.")
            exit()
        addStudent(str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]))
        
    # Update
    if not action or action.lower() == "u" or action.lower() == "update":
        if len(sys.argv) < 4:
            print("Not enough arguments. Please provide student ID, and the new email.")
            exit()
        updateStudentEmail(str(sys.argv[2]), str(sys.argv[3]))
        
    # Delete
    if not action or action.lower() == "d" or action.lower() == "delete":
        if len(sys.argv) < 3:
            print("Not enough arguments. Please provide student ID.")
            exit()
        deleteStudent(str(sys.argv[2]))

if __name__ == "__main__":
    main()

connection.commit()
connection.close()