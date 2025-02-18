lst=[("carrot","potato"),(220,1000)]
lst[0]=list(lst[0])
lst[1]=list(lst[1])
for i in range(len(lst[1])):
    for j in range(1,len(lst[1])):
        if lst[1][j-1]<lst[1][j]:
            lst[1][j - 1],lst[1][j]=lst[1][j],lst[1][j-1]
            lst[0][j-1],lst[0][j]=lst[0][j],lst[0][j-1]
lst[0]=tuple(lst[0])
lst[1]=tuple(lst[1])

print(lst)