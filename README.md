# PostgreSQL CRUD Program

Isaac Robert
March 18, 2024

Create the A3 database using pgAdmin4, then with the query tool open the file init.sql and run it with the
pgAdmin GUI. This will generate the Students table and populate it with the sample data.

In a terminal use
```
python interface.py <arg>
```
and run the application with the desired arguments:
- C/create runs addStudent(first_name, last_name, email, enrollment_date): Inserts a new student record into the students table.
- R/read runs getAllStudents(): Retrieves and displays all records from the students table.
- U/update runs updateStudentEmail(student_id, new_email): Updates the email address for a student with the specified student_id.
- D/delete runs deleteStudent(student_id): Deletes the record of the student with the specified student_id.
      
*Note: running without an argument will run all the functions on the Students table*

Eerror handling is provided shoul you attempt to use an operation without supplying enough arguments

Sample Commands:
```
python interface.py create Machine Jack machinejack@example.com 2024-01-01
```
```
python interface.py read
```
```
python interface.py update 4 newemailimadeup@example.com
```
```
python interface.py delete 4
```

demonstration of the program:
https://youtu.be/xtxumtjTD00

![image](https://github.com/Friendly-Neighborhood-Programmer/postgresql-crud-interface/assets/100625812/38466c64-4367-450a-b2aa-5e64f3e6b4fa)

![image](https://github.com/Friendly-Neighborhood-Programmer/postgresql-crud-interface/assets/100625812/c7467b54-febd-47cc-a072-ce08a69dc31e)

![image](https://github.com/Friendly-Neighborhood-Programmer/postgresql-crud-interface/assets/100625812/4ad19dcb-1630-4605-bf68-8d50036bf8f8)

![image](https://github.com/Friendly-Neighborhood-Programmer/postgresql-crud-interface/assets/100625812/4c7386f7-e203-409b-a5b7-e836f16c82fc)

![image](https://github.com/Friendly-Neighborhood-Programmer/postgresql-crud-interface/assets/100625812/c6f42a6e-5c43-4a82-b41b-d5c04c210dcf)
