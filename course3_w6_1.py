import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Parsing url
url = input("Enter location: ")
# Test Link: url = "http://py4e-data.dr-chuck.net/comments_42.json"
print("Retrieving:", url)
url_data = urllib.request.urlopen(url, context=ctx).read()

# Parse URL using json.loads
info = json.loads(url_data)

# Extract comments from dictionary using loop, define starting point
list = list()
for u in info['comments']:
    num = int(u['count'])
    list.append(num)

print('Count:', len(list))
print('Sum:', sum(list))
