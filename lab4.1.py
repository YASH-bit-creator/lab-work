def swap_case(string):
    str1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str2='abcdefghijklmnopqrstuvwxyz'
    new=''
    for i in range(len(string)):
        if string[i] in str1:
            index=str1.index(string[i])
            new+=str2[index]
        else:
            index = str2.index(string[i])
            new += str1[index]
    print(new)

string= input("enter a string ")
swap_case(string)
