Isaac Robert
March 18, 2024

- create the A3 database using pgAdmin4, then with the query tool open the file init.sql and run
it with the pgAdmin GUI.
This will generate the Students table and populate it with the sample data.

- open a terminal and run 'python interface.py <arg>', this will run the application with the
required functions you choose: getAllStudents(), addStudent(), updateStudentEmail(), deleteStudent()

- program 'interface.py <arg>' can be run with the following arguments:
    - c/create runs addStudent()
    - r/read getAllStudents() with the additionally supplied arguments
    - u/update runs updateStudentEmail() with the additionally supplied arguments
    - d/delete runs deleteStudent() with the additionally supplied arguments
    Note: running without an option will run all the functions on the Students table. 

Sample Commands:
python interface.py create Machine Jack machinejack@example.com 2024-01-01
python interface.py read
python interface.py update 4 newemailimadeup@example.com
python interface.py delete 4

demonstration of the program:
https://youtu.be/xtxumtjTD00