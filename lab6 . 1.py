students=[("yash","swayam"),"gita","sunita","chashmita",("shivam","shiv")]
boys=0
girls=0
for i in range(len(students)):
    if type(students[i])==tuple:
        for j in range(len(students[i])):
            boys+=1
    else:
        girls+=1
print(f"number of girls : {girls}\n number of boys : {boys}")