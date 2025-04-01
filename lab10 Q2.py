
file1=open("file.csv",'r')
read=file1.readlines()
d={}
for j in read[1:]:
    i=j.strip().split(",")
    lst=[i[0],int(i[2]),int(i[3]),int(i[4]),int(i[2])+int(i[3])+int(i[4])]
    d[i[1]]=lst
print(d)


