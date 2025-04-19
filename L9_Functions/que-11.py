def creat_list(l1,l2):
    l1 = set(l1)
    l2 = set(l2)
    l3 = list(l1 & l2)
    return l3

l1 = [1,2,3,4,6,7,8,9,0]
l2 = [9,3,5,7,1]
print(creat_list(l1,l2))