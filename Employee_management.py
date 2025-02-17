import mysql.connector
from flask import Flask, request
 
class Employee:
    unique_ids = set()
 
    def __init__(self, employee_id, name, department):
        if employee_id in Employee.unique_ids:
            raise ValueError("Employee ID must be unique")
        self.employee_id = employee_id
        self.name = name
        self.department = department
        Employee.unique_ids.add(employee_id)
 
    def display_employee(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"
 
def create_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="kruti@220",
        database="signifydb"
    )
    return conn
 
def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        id INT PRIMARY KEY,
        name VARCHAR(30),
        department VARCHAR(30)
    )""")
    conn.commit()
    cursor.close()
    conn.close()
 
def add_employee_to_db(employee):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Employee (id, name, department) VALUES (%s, %s, %s)",
                   (employee.employee_id, employee.name, employee.department))
    conn.commit()
    cursor.close()
    conn.close()
 
app = Flask(__name__)
create_table()
 
@app.route('/')
def home():
    return "Welcome to Employee Management System"
 
@app.route('/add_employee')
def add_employee():
    try:
        emp_id = int(request.args.get('employee_id'))
        name = request.args.get('name')
        department = request.args.get('department')
        employee = Employee(emp_id, name, department)
        add_employee_to_db(employee)
        return "Employee added successfully"
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Error: {str(e)}"
 
if __name__ == '__main__':
    app.run(debug=True)
