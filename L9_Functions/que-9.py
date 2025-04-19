def count_alpha_digits(s):
    d = {}
    for i in range(len(s)):
        if (s[i] not in d.keys()):
            d[s[i]] = 1
        else :
            d[s[i]] += 1
    return d

st = input("Enter a string : ")
print(count_alpha_digits(st))