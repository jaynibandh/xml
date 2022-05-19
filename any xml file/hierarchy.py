
from encodings import utf_8
import xml.etree.ElementTree as ET
k=[]
f=open("j","w",encoding="utf-8")
def perf_func(elem, func, level=0):
    func(elem,level)
    for child in list(elem):
        perf_func(child, func, level+1)



def print_level(elem,level):
    #print ('-'*level+elem.tag)
    #print(level)
    f.write("\n"+str(level)+" "+elem.tag)
    f.write("\n"+str(elem.attrib))

  #k.append(('-'*level+elem.tag))
  #print(k)
  #return k

root = ET.parse('US2022030732A1.xml')
k=perf_func(root.getroot(), print_level)

f = open('j','r',encoding="utf_8")
separatoe=list(f.read().split("\n"))
o=[i.split(' ') for i in separatoe] 
#print(o)
r=0
while r<len(o):
    if r==len(o)-1:
        #print (o[r][1])
        break
    print (r)
    
    print(":"+o[r+1][0])
    print(" "+":" +" "+o[r+1][1])
    if o[r+1][1]=="invention-title":
        break
    r=r+1
print()
k=o[1][1]
print(k)
print(len(o))