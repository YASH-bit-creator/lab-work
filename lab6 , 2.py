
list1=[("24bit057","24bit073"),("yash","swayam"),(123,423)]
rollno=[]
names=[]
age=[]

for j in range(len(list1[1])):
    names.append(list1[1][j])
for j in range(len(list1[0])):
    rollno.append(list1[0][j])
for j in range(len(list1[2])):
    age.append(list1[2][j])

print(rollno,age,names)