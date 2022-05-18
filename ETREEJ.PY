from os import remove
from pickle import NONE, TRUE
import xml.etree.ElementTree as ET
import re
import csv
import string
i=0
from bs4 import BeautifulSoup
""" xmlData = None

xmlFile = open('C:/Users/Jayanth/Downloads/check.xml', 'r')
xmlData = xmlFile.read()

soup = BeautifulSoup(xmlData, 'xml')
ja = soup.br.decompose()
#print (ja)
"""
regex = r"(?i)<br */?>"
subst = "\\n"
"""with open ('C:/Users/Jayanth/D/check.xml', 'r' ) as f:
    content = f.read()
 
    content_new = re.sub(regex, subst, content, 0)"""
count=0
#reg=regex(r'/n[A-Z][A-Z]')
xmlTree = ET.parse('C:/Users/Jayanth/Downloads/check.xml')
tags = {elem.tag for elem in xmlTree.iter()}
print (tags)
tree_root = xmlTree.getroot()
f = open("patent.txt", "w",encoding="utf-8")
q=open("jja.txt","w",encoding="utf-8")
print(tree_root)
if len(tree_root):   
 print(len(tree_root))
k=tree_root.findall("DOCUMENT/DESC")

print(len(k))
k=tree_root.findall("DOCUMENT/CLMS")

print(len(k))
k=tree_root.findall("DOCUMENT/TI")

print(len(k))

k=tree_root.findall("DOCUMENT/AB")

print(len(k))
for node in xmlTree.iter('DOCUMENT'):
    for ele in node.iter():
        if not ele.tag==node.tag:
            
            if ele.tag=="TI":
             count=count+1
             if count==len(tree_root):
                 break
             f.write("TITLE NO:")

            
             f.write(str(count))
             f.write("\n")
             ##print("{}:{}".format(ele.tag,ele.text))
             f.write("{}:{}".format(ele.tag,ele.text))  
             f.write("\n")           
            if ele.tag=="PDG":
             ##print("{}:{}:{}".format(ele.tag,ele.attrib,ele.text)) 
             f.write("{}:{}:{}".format(ele.tag,ele.attrib,ele.text))
             f.write("\n")
            if ele.tag=="FAN":
             #print("{}:{}".format(ele.tag,ele.text))
             f.write("{}:{}".format(ele.tag,ele.text))
             f.write("\n")
            if ele.tag=="AB":
             #print("{}:{}:{}".format(ele.tag,ele.attrib,ele.text))
             f.write("{}:{}:{}".format(ele.tag,ele.attrib,ele.text))
             f.write("\n")
            if ele.tag=="CLMS":

             ##print("{}".format(ele.tag))  
             f.write("{}".format(ele.tag))
             k=ele.attrib
             f.write("\n")
             ##print(''.join(tree_root.find("DOCUMENT/CLMS").itertext()))
             ace='\n'.join(tree_root.findall("DOCUMENT/CLMS")[count-1].itertext())
             #print (ace)
             f.write(ace)
             f.write("\n") 
             #print("##############################")
             #print(ace)


             #print("***********************************GG************************")


            #print("##############################")
            if ele.tag=="DESC":
             
             #print("{}".format(ele.tag)) 
             f.write("{}".format(ele.tag))
             q.write("{}".format(ele.tag))
             f.write("\n")
             q.write("\n")
             #print(''.join(tree_root.find("DOCUMENT/DESC").itertext()))
       
             pay="\n".join(tree_root.findall("DOCUMENT/DESC")[count-1].itertext())
             #print(pay)
             f.write(pay) 
             q.write(pay) 
             
             f.write("\n")
             #q.write("\n")

            if ele.tag=="CPC":
             #print("{}:{}".format(ele.tag,ele.text)) 
             f.write("{}:{}".format(ele.tag,ele.text))
             f.write("\n")
           
match = re.findall(r"\b([?=[A-ZA-Z]*[A-Z])[A-Z]{2,}",str(pay) ) 
#print("*******************")
#print(match)
f=open("a.txt","w",encoding="utf-8")
f.write(("\n").join(match))
f.close()
#print("*************")

f.close()
separate=list(pay.split(" "))
f=open("lode.txt","w",encoding="utf-8")
while i<=len(separate)+1:

 i=i+1
 if i==len(separate):
     break
 if separate[i].isupper() and separate[i-1].isupper():
               f.write("{")
               f.write(separate[i-1])
               k=separate[i-1]
               #print(separate[i-1])
               f.write(":")
               f.write(str(i-1))
               f.write("}")
 if separate[i].isupper() and separate[i-1].isupper():
     

                j=separate[i]
                if k==j:
                 f.write("{")
                 f.write(separate[i])
                 #print(separate[i])
                 f.write(":")
                 f.write(str(i))
                 f.write("}")
    
 if separate[i].isupper() and separate[i-2].isupper():
                l=separate[i]
                if l==j:
                 f.write("{")
                 f.write(separate[i])
                 #print(separate[i])
                 f.write(":")
                 f.write(str(i))
                 f.write("}")
    

f=open("lode.txt","r",encoding="utf-8")
separatoe=list(f.read().split("'"))
             
f=open("lode1.txt","w",encoding="utf-8")
res = [i for n, i in enumerate(separatoe) if i not in separatoe[:n]]
re1s=(" ".join(res))
f.write(re1s)
f.close()
f.close()

match = re.findall(r"^([A-Z][A-Z]*([A-Z])+(.)+[A-Z]*?)$\n",str(pay) ) 
#print(match)


""" for c in node.iter():
                   #print(         f.write(''.join(tree_root.find("DOCUMENT/DESC").itertext()))  
"""
