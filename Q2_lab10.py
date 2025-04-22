filename = "students.csv"

records = {}

with open(filename, "r") as file:
    lines = file.readlines()
    header = lines[0].strip().split(',')  # ['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3']
    
    for line in lines[1:]:
        parts = line.strip().split(',')
        rollno = int(parts[0])
        name = parts[1]
        marks = list(map(int, parts[2:5]))
        total = sum(marks)
        
        records[rollno] = {
            'Name': name,
            'Marks': marks,
            'Total': total
        }

# Display dictionary data
for roll, data in records.items():
    print(f"Roll No: {roll}, Name: {data['Name']}, Marks: {data['Marks']}, Total: {data['Total']}")
