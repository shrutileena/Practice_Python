import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter location: ")
xml = urllib.request.urlopen(url).read()
print("retrieving", url)

#stuff = xml.dom.minidom.parse(xml)
stuff = ET.fromstring(xml)
print("Retrieved", len(xml), "characters")
lst = stuff.findall('comments/comment')
print("Count:", len(lst))

numbers = list()
addition = 0

for item in lst:
    numbers.append(item.find('count').text)

for i in numbers:
    addition += int(i)

print("Sum:", addition)