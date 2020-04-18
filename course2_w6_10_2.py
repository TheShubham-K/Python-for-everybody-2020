name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
timestamp = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    line = line.split()
    line = line[5]
    line = line.split(":")
    line = line[0]
    #print(line)
    timestamp[line] = timestamp.get(line, 0) + 1
    #print(line,timestamp[line])
#print(timestamp)

tmp = list()
for k,v in timestamp.items() :
    #print(k,v)
    newt = (k,v)
    tmp.append(newt)

tmp = sorted(tmp)
# print(tmp)

for v,k in tmp:
    print(v,k)

# bigcount = None
# bigword = None
# for word,count in emailaccount.items():
#    if bigcount == None or count > bigcount:
#        bigcount = count
#        bigword = word
# print(bigword, bigcount)
