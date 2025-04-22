src=open("source.txt", "r")#source file 
destination=open("destination.txt", "w")#destination file
for line in src:
    destination.write(line.upper())