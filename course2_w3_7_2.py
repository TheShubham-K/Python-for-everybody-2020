# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0.0
tot = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    line = line.rstrip()
    line = line[20:]
    fline = float(line)
    tot = tot + fline
    count = count + 1

#print("Done")
#print(count)
print("Average spam confidence:",tot/count)
