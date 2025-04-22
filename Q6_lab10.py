f1=open("file1.txt")  
f2=open("file2.txt") 
destination=open("merged.txt", "w") 
lines1 = f1.readlines()
lines2 = f2.readlines()
max_len = max(len(lines1), len(lines2))

for i in range(max_len):
    if i < len(lines1):
        destination.write(lines1[i])
    if i < len(lines2):
        destination.write(lines2[i])
