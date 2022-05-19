from os import remove
from pickle import NONE, TRUE
import xml.etree.ElementTree as ET
import re
import csv
import string

from encodings import utf_8
import xml.etree.ElementTree as ET
i=0
from bs4 import BeautifulSoup
""" xmlData = None

xmlFile = open('C:/Users/Jayanth/Downloads/check.xml', 'r')
xmlData = xmlFile.read()

soup = BeautifulSoup(xmlData, 'xml')
ja = soup.br.decompose()
print (ja)
"""
regex = r"(?i)<br */?>"
subst = "\\n"
"""with open ('C:/Users/Jayanth/D/check.xml', 'r' ) as f:
    content = f.read()
 
    content_new = re.sub(regex, subst, content, 0)"""
count=0
#reg=regex(r'/n[A-Z][A-Z]')
xmlTree = ET.parse('US2022030732A1.xml')
tags = {elem.tag for elem in xmlTree.iter()}
#print (tags)
j=("\n").join(tags)
print(j)
ki=j.split()
print(ki)
print(len(tags))
tree_root = xmlTree.getroot()
f = open("adult.txt", "w",encoding="utf-8")
print(tree_root.findall("patent-document"))


if len(tree_root):   
 print(len(tree_root))
count=0
c=0


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
        print (o[r][0])
        break
    print(o[r+1][0])
    print(o[r+1][1])
    
    r=r+1

for node in xmlTree.iter('patent-document'):
    for ele in node.iter():
        if not ele.tag==node.tag:
            #k=ele.tag
            #for jone in xmlTree.iter('patent-document'):
              #for jin in jone.iter():
                #if not jin.tag==jone.tag:
                    #count=count+1
            #if count==: 
            #break            
            #print("{}:{}".format(ele.tag,ele.attrib))
            #l=("").join(ele.tag)
            #k=tree_root.find(ele.tag)
                    #if ele.tag==jin.tag:
                     #c=c+1
                    #else:
                        #print(ele.tag)
                        #print(jin.tag)                     
            #pay="\n".join(tree_root.findall(ele.tag).itertext())

            #f.write(pay)
            print("{}:{}".format(ele.tag,ele.text))
            f.write(str(ele.tag))
            f.write(" : ")
            f.write(str(ele.text))
            f.write('\n')
            f.write("\n")
             ##print(''.join(tree_root.find("DOCUMENT/CLMS").itertext()))
            ace='\n'.join(tree_root.findall()[count-1].itertext())
             #print (ace)
            f.write(ace)
            f.write("\n") 
            