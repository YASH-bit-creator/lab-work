def frequency(s):
    l = s.split()
    d = {}
    for ele in l:
        if ele in d.keys():
            d[ele] += 1
        else :
            d[ele] = 1
    return d

st = input("Enter a string : ")
print(frequency(st))