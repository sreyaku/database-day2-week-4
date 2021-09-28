import sqlite3
conn = sqlite3.connect("Employee.db")
cursor = conn.cursor()

# a) Create a Table Employee which will have the four columns - Name, ID, salary, and Department_id.

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

cursor.execute("""CREATE TABLE EMPLOYEE (NAME TEXT, ID INTEGER,SALARY INTEGER,DEPARTMENT_ID INTEGER)""")

print("Table created")

# b) Add a new column ‘City’ to the Table Employee.

cursor.execute("ALTER TABLE EMPLOYEE ADD CITY TEXT")

print("Table altered")

conn.commit()

# c) Insert 5 records into this table.
for i in range(0, 5):
    employee_det = (input("Enter the ID of Employee:"), input('Enter the Name of the Employee:'),
                    input("Enter the Salary of the Employee:"), input("Enter the Department_Id of the employee:"))
    cursor.execute("""INSERT INTO EMPLOYEE(ID,Name,salary,Department_id)VALUES(?,?,?,?)""", employee_det)

cursor.execute("""SELECT rowid,* FROM EMPLOYEE""")
result = cursor.fetchall()

print("\n ID,Name,salary And Department_id of the employee:")
for item in result:
    print(item[0], item[1], item[2], item[3],item[4])

conn.commit()
# values = [('sandra', 101, 20000, 1, 'New York'), ('Peter', 102, 30000, 2, 'Washington'),
#           ('Sammy', 103, 35000, 2, 'Los Angles'),
#           ('Linda', 104, 25000, 3, 'california'), ('John', 105, 30000, 1, 'Georgia')]
# cursor.executemany("INSERT INTO EMPLOYEE VALUES (?,?,?,?,?)", values)
# conn.commit()


# d) Read the Name, ID, and Salary from the Employee table and print it

def employee_record():
    cursor.execute("SELECT NAME,ID,SALARY FROM EMPLOYEE")

    record = cursor.fetchall()

    for row in record:
        print("\nName:", row[0])

        print("ID:", row[1])

        print("Salary:", row[2])


# e) Print the details of employees whose names start with ‘j’ (or any letter input by the user)

def employee_details(e_name):
    cursor.execute("SELECT * FROM EMPLOYEE WHERE NAME LIKE '" + e_name + "%'")

    result = cursor.fetchall()

    # print(result)

    if len(result) == 0:

        print(f"No employee whose name starts with {e_name}")

    else:

        print(f"Employee details whose name starts with {e_name} are:")

        for row in result:
            print("\nName:", row[0])

            print("ID:", row[1])

            print("Salary:", row[2])

            print("Department_id:", row[3])

            print("City:", row[4])


# f)Print the details of employees with ID’s inputted by the user.

def employee_details_id(id):
    cursor.execute("SELECT * FROM EMPLOYEE WHERE ID =:e_id", {"e_id": id})

    result = cursor.fetchall()

    print(f"Employee details whose name starts with {id} are:")

    for row in result:
        print("\nName:", row[0])

        print("ID:", row[1])

        print("Salary:", row[2])

        print("Department_id:", row[3])

        print("City:", row[4])


# g)Change the name of the employee whose ID is input by the user.

def change_name(em_id, e_name):
    cursor.execute("SELECT NAME FROM EMPLOYEE WHERE ID =:id", {"id": em_id})

    result = cursor.fetchone()

    print("Name of Employee before Update:", result[0])

    cursor.execute("UPDATE EMPLOYEE SET NAME =:name WHERE ID =:id", {"name": e_name, "id": em_id})

    print("Name changed")

    cursor.execute("SELECT NAME FROM EMPLOYEE WHERE ID =:id", {"id": em_id})

    result = cursor.fetchone()

    print("Name of Employee after Update:", result[0])


var = True

while var:

    print(

        "\n 1.Employee Record\n 2..Employee details\n 3.Employee details with ID\n 4.To Change the Employee Name\n "

        "5.exit")

    ch = int(input("Enter the choice:"))

    if ch == 1:
       employee_record()

    elif ch == 2:

        user_input = input("Enter the letter:")
        employee_details(user_input.capitalize())

    elif ch == 3:

        user_input = int(input("Enter the ID:"))
        employee_details_id(user_input)

    elif ch == 4:
         user_input = int(input("Enter the id of employee to change the name:"))
         name = input("Enter the name you want:")
         change_name(user_input, name.capitalize())

    elif ch == 5:
          var = False

conn.commit()
conn.close()
