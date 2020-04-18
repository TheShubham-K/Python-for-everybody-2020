import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Parsing url
url = input("Enter location: ")
print("Retrieving:", url)
uh = urllib.request.urlopen(url, context=ctx).read()

# Count length of data and printing it
print("Retrieved", len(uh),"characters")

# Producing structure of grabbing the tree of nodes: deserialization
tree = ET.fromstring(uh)

# Grab all the count nodes
comments = tree.findall(".//comment")

# Creating Variables
lst = list()
counttotal = 0

# Extract comment counts from XML using loop
for item in comments:
    count = item.find("count").text
    count = int(count)
    counttotal = counttotal + 1
    lst.append(count)

# Printing Results
print("Count:", counttotal)
print("Sum:",sum(lst))
