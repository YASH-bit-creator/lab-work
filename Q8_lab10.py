remove_words = {'a', 'an', 'the'}

f1=open("input.txt", "r") 
f2=open("output.txt", "w") 
for line in f1:
    words = line.split()
    filtered = [word for word in words if word.lower() not in remove_words]
    f2.write(" ".join(filtered) + "\n")
