n=int(input("enter the number of students:"))

lst=[]
for _ in range(n):
    name=input(f"enter the name of student{_+1} : ")
    roll_num=input(f"enter the roll number of student{_+1} : ")
    data=[name,roll_num]
    lst.append(data)
with open("file.csv",'w') as file:
    for i in range(n):
        file.write(f"{lst[i][0]},{lst[i][1]}\n")
file.close()
