name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
emailaccount = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    line = line[1]
    #print(line)
    emailaccount[line] = emailaccount.get(line, 0) + 1
    #print(line,emailaccount[line])

bigcount = None
bigword = None
for word,count in emailaccount.items():
    if bigcount == None or count > bigcount:
        bigcount = count
        bigword = word
print(bigword, bigcount)
