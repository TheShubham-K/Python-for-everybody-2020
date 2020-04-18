import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
handle = open(name)
numlist = list()
sum = 0

for line in handle:
    stuff = re.findall("[0-9]+", line)
    if len(stuff) < 1: continue
    #print(stuff)
    for strnums in stuff:
        sum = sum + int(strnums)
print(sum)
