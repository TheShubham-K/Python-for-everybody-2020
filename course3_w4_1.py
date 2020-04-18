# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("span")
sum = 0
count = 0
for tag in tags:
    # Look at the parts of a tag
    # print("TAG:", tag)
    # print("URL:", tag.get("comments", None))
    # print("Contents:", tag.contents[0])
    # print("Attrs:", tag.attrs)
    sum = sum + int(tag.contents[0])
    count = count + 1
print("Count", count)
print("Sum", sum)
