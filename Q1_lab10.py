import csv

with open('students.csv', mode='x', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerow([1, 'Alice', 85, 78, 92])
    writer.writerow([2, 'Bob', 90, 88, 76])
