# Define the Employee class
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def display(self):
        print(f"Code: {self.empcode}, Name: {self.empname}, DOJ: {self.doj}, Salary: {self.salary}")

# Create an object of Employee
emp = Employee("E101", "Alice", "2022-06-01", 50000)

# Serialize 
with open("employee.txt", "w") as file:
    file.write(f"{emp.empcode},{emp.empname},{emp.doj},{emp.salary}\n")

# Deserialize 
with open("employee.txt", "r") as file:
    data = file.readline().strip().split(',')
    empcode, empname, doj, salary = data[0], data[1], data[2], float(data[3])
    deserialized_emp = Employee(empcode, empname, doj, salary)

# Display the deserialized object
deserialized_emp.display()
