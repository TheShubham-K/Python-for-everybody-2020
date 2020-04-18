x = "From marquard@uct.ac.za"
y = str.find(x,"uct")
print(y)
print(x[14:17])

print(len('banana')*7)

greet = "Hello Bob"
print(greet.upper())

data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
pos = data.find(".")
print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475";
snum = text.find("0")
fnum = float(text[snum:snum+6])
print(fnum)
