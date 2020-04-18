import re

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From ") :
        continue
    line = line.rstrip()
    words = re.split(" |@",line)
    email = words[2]
    count = count+1
    print(email)

print("There were", count, "lines in the file with From as the first word")
