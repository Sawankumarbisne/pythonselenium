import xml.dom.minidom
from xml.dom.minidom import Node

dom = xml.dom.minidom.parse("C:\\Users\\Settings.xml")

def getChildrenByTitle(node):
    for child in node.childNodes:
        if child.localName=='SettingsEntry':
            yield child
Topic = dom.getElementsByTagName('Value')
i=0
alist=[]
for node in Topic:
    alist.insert(i,node.childNodes[0].nodeValue)
    i= i+1
url=alist[0]
username=alist[1]
password=alist[2]
spath=alist[3]

print(url)
print(username)
print(password)
print(spath)