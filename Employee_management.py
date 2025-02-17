import mysql.connector

def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kruti@22",
        database="signifydb"
    )
    return conn

def create_table(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Employee (
        id INT PRIMARY KEY,
        name VARCHAR(30),
        age INT
    )
    """
    cursor.execute(create_table_query)

def add_employee(cursor, conn):
    try:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        query = "INSERT INTO Employee (id, name, age) VALUES (%s, %s, %s)"
        cursor.execute(query, (emp_id, name, age))
        conn.commit()
        print("Employee added successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and age.")

def view_employees(cursor):
    query = "SELECT * FROM Employee"
    cursor.execute(query)
    records = cursor.fetchall()
    if records:
        print("\n--- Employee Records ---")
        for emp in records:
            print(f"ID: {emp[0]}, Name: {emp[1]}, Age: {emp[2]}")
    else:
        print("No employees found.")

def update_employee(cursor, conn):
    try:
        emp_id = int(input("Enter employee ID to update: "))
        new_name = input("Enter new name: ")
        new_age = int(input("Enter new age: "))
        query = "UPDATE Employee SET name = %s, age = %s WHERE id = %s"
        cursor.execute(query, (new_name, new_age, emp_id))
        if cursor.rowcount == 0:
            print("Employee not found.")
        else:
            conn.commit()
            print("Employee updated successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    except ValueError:
        print("Invalid input. Please enter numeric values for ID and age.")

def delete_employee(cursor, conn):
    try:
        emp_id = int(input("Enter employee ID to delete: "))
        query = "DELETE FROM Employee WHERE id = %s"
        cursor.execute(query, (emp_id,))
        if cursor.rowcount == 0:
            print("Employee not found.")
        else:
            conn.commit()
            print("Employee deleted successfully.")
    except mysql.connector.Error as err:
        print("Error:", err)
    except ValueError:
        print("Invalid input. Please enter a numeric value for ID.")

def main():
    conn = create_connection()
    cursor = conn.cursor()
    create_table(cursor)
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_employee(cursor, conn)
        elif choice == '2':
            view_employees(cursor)
        elif choice == '3':
            update_employee(cursor, conn)
        elif choice == '4':
            delete_employee(cursor, conn)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
    cursor.close()
    conn.close()
    print("Goodbye!")

if __name__ == '__main__':
    main()
